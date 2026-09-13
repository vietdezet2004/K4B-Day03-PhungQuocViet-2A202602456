"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
import sys
from typing import Dict, Any

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Đã được định nghĩa mẫu sẵn cho Học viên tham khảo
    {
        "name": "academic_query",
        "description": "Tra cứu hồ sơ và thông tin học vụ của sinh viên VinUni bằng mã sinh viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu (ví dụ: 'SV2026001')"
                }
            },
            "required": ["student_id"]
        }
    },
    
    # --------------------------------------------------------------------------
    # TODO 1.2: HỌC VIÊN HOÀN THIỆN TOOL SCHEMA CHO 'schedule_appointment'
    # 🎯 YÊU CẦU THIẾT KẾ SCHEMA (JSON SCHEMA STANDARD):
    # 1. Tool dùng để đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.
    # 2. Thiết kế các tham số (properties) để LLM trích xuất:
    #    - student_id (string): Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')
    #    - datetime_str (string): Thời gian hẹn (ví dụ: '14:00 15/09/2026')
    #    - advisor_name (string): Tên cố vấn học tập
    # 3. Khai báo danh sách các trường bắt buộc (required).
    # --------------------------------------------------------------------------
    {
        "name": "schedule_appointment",
        "description": "Đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần đặt lịch hẹn (ví dụ: 'SV2026001')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn tư vấn (ví dụ: '14:00 15/09/2026')"
                },
                "advisor_name": {
                    "type": "string",
                    "description": "Tên cố vấn học tập cần gặp (ví dụ: 'PGS.TS Nguyễn Văn A')"
                }
            },
            "required": ["student_id", "datetime_str"]
        }
    },
    # Tool 3 (VinBus): Tra cứu lộ trình xe bus điện
    {
        "name": "bus_route_query",
        "description": "Tra cứu lộ trình, các trạm dừng, thời gian hoạt động và giá vé của tuyến xe bus điện VinBus bằng mã tuyến (ví dụ: 'E01', 'E03', 'E09').",
        "parameters": {
            "type": "object",
            "properties": {
                "route_id": {
                    "type": "string",
                    "description": "Mã tuyến xe bus điện cần tra cứu (ví dụ: 'E01', 'E09')"
                }
            },
            "required": ["route_id"]
        }
    },
    # Tool 4 (VinBus): Đăng ký vé tháng xe bus điện
    {
        "name": "register_monthly_pass",
        "description": "Đăng ký làm vé tháng xe bus điện VinBus cho khách hàng.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Họ và tên của khách hàng đăng ký vé tháng"
                },
                "phone_number": {
                    "type": "string",
                    "description": "Số điện thoại liên hệ của khách hàng"
                },
                "route_id": {
                    "type": "string",
                    "description": "Mã tuyến xe bus điện cần đăng ký vé tháng (ví dụ: 'E01', 'E09')"
                },
                "start_date": {
                    "type": "string",
                    "description": "Ngày bắt đầu áp dụng vé tháng (ví dụ: '01/10/2026')"
                }
            },
            "required": ["customer_name", "route_id"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "SV2026001": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A"
    },
    "SV2026002": {
        "full_name": "Trần Thị Bình",
        "class": "AI-K4",
        "gpa": 3.60,
        "email": "binh.tt@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "TS. Lê Thị B"
    }
}

VINBUS_DATABASE = {
    "E01": {
        "route_name": "Tuyến E01: Bến xe Mỹ Đình - Khu đô thị Vinhomes Ocean Park",
        "operating_hours": "05:00 - 21:00 (hằng ngày)",
        "frequency": "15 - 20 phút/chuyến",
        "ticket_price": "8.000 VNĐ/lượt",
        "stops": "Bến xe Mỹ Đình - Phạm Hùng - Khuất Duy Tiến - Nguyễn Trãi - Cầu Vĩnh Tuy - Vinhomes Ocean Park",
        "status": "Đang hoạt động"
    },
    "E03": {
        "route_name": "Tuyến E03: Khu liên cơ quan Sở ngành Hà Nội - Vinhomes Ocean Park",
        "operating_hours": "05:05 - 21:00",
        "frequency": "15 - 20 phút/chuyến",
        "ticket_price": "9.000 VNĐ/lượt",
        "stops": "Khu liên cơ quan - Võ Chí Công - Cầu Nhật Tân - Long Biên - Vinhomes Ocean Park",
        "status": "Đang hoạt động"
    },
    "E09": {
        "route_name": "Tuyến E09: Khu đô thị Vinhomes Smart City - Công viên nước Hồ Tây",
        "operating_hours": "05:00 - 21:00",
        "frequency": "15 - 20 phút/chuyến",
        "ticket_price": "9.000 VNĐ/lượt",
        "stops": "Vinhomes Smart City - Đại lộ Thăng Long - Lê Trọng Tấn - Phạm Văn Đồng - Lạc Long Quân - Công viên nước Hồ Tây",
        "status": "Đang hoạt động"
    }
}


def execute_academic_query(student_id: str) -> str:
    """Thực thi tra cứu học vụ theo mã sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if student:
        return json.dumps({
            "status": "SUCCESS",
            "student_id": student_id,
            "data": student
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)


def execute_schedule_appointment(student_id: str, datetime_str: str, advisor_name: str = "PGS.TS Nguyễn Văn A") -> str:
    """Thực thi đặt lịch hẹn tư vấn học vụ"""
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-{student_id}-99",
        "student_id": student_id,
        "datetime": datetime_str,
        "advisor": advisor_name,
        "message": f"Đặt lịch thành công cho sinh viên {student_id} với {advisor_name} vào lúc {datetime_str}."
    }, ensure_ascii=False)


def execute_bus_route_query(route_id: str) -> str:
    """Thực thi tra cứu lộ trình tuyến xe bus điện VinBus"""
    route = VINBUS_DATABASE.get(route_id.strip().upper())
    if route:
        return json.dumps({
            "status": "SUCCESS",
            "route_id": route_id.upper(),
            "data": route
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy thông tin tuyến xe bus điện '{route_id}'. Tuyến xe này hiện chưa vận hành hoặc không tồn tại trong hệ thống VinBus."
        }, ensure_ascii=False)


def execute_register_monthly_pass(customer_name: str, route_id: str, phone_number: str = "", start_date: str = "01/10/2026") -> str:
    """Thực thi đăng ký vé tháng xe bus điện VinBus"""
    ticket_code = f"VB-{route_id.upper()}-{phone_number[-4:] if len(phone_number)>=4 else '8888'}"
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": ticket_code,
        "customer_name": customer_name,
        "phone_number": phone_number,
        "route_id": route_id.upper(),
        "start_date": start_date,
        "message": f"Đăng ký vé tháng VinBus thành công cho khách hàng {customer_name} (SĐT: {phone_number}) cho tuyến {route_id.upper()}, có hiệu lực từ ngày {start_date}. Mã vé điện tử: {ticket_code}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "academic_query": execute_academic_query,
    "schedule_appointment": execute_schedule_appointment,
    "bus_route_query": execute_bus_route_query,
    "register_monthly_pass": execute_register_monthly_pass
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    try:
        if tool_name == "academic_query":
            return execute_academic_query(**arguments)
        elif tool_name == "schedule_appointment":
            return execute_schedule_appointment(**arguments)
        elif tool_name in ["bus_route_query", "route_query"]:
            return execute_bus_route_query(**arguments)
        elif tool_name in ["register_monthly_pass", "book_monthly_pass"]:
            return execute_register_monthly_pass(**arguments)
        elif tool_name in TOOL_ROUTER:
            return TOOL_ROUTER[tool_name](**arguments)
        else:
            return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)


if __name__ == "__main__":
    print("==========================================================")
    print("🛠️ KIỂM THỬ ĐỘC LẬP TOOLS LAYER (src/tools.py)")
    print("==========================================================")
    print(f"✅ [TOOLS CHECK]: Đã đăng ký thành công {len(TOOLS_SCHEMA)} Native Tools trong TOOLS_SCHEMA!")
    
    test_raw = dispatch_tool_call("academic_query", {"student_id": "SV2026001"})
    test_res = json.loads(test_raw)
    student_name = test_res.get("data", {}).get("full_name", "Nguyễn Văn An")
    print(f"🧪 Kết quả gọi thử academic_query: Status {test_res.get('status')} (Sinh viên {student_name})")
    print(f"   Dữ liệu chi tiết: {json.dumps(test_res, ensure_ascii=False)}")
