# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Phùng Quốc Việt  
> **Mã Sinh Viên / Mã Học viên:** 2A202602456  
> **Chủ đề Lựa chọn:** Trợ lý Dịch vụ Khách hàng VinBus: Tra cứu lộ trình tuyến xe bus điện và đăng ký vé tháng. (Gợi ý 4.2)  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Bài toán yêu cầu chuỗi suy luận nhiều bước có tính xâu chuỗi: (1) Tiếp nhận nhu cầu di chuyển hoặc thông tin khách hàng -> (2) Tra cứu lộ trình tuyến xe bus điện VinBus phù hợp với điểm đi/điểm đến -> (3) Kiểm tra giá cước, chính sách ưu đãi cho đối tượng (học sinh/sinh viên/người cao tuổi) -> (4) Khởi tạo yêu cầu đăng ký vé tháng với thông tin cá nhân và tuyến tương ứng. |
| **2. Tool Interaction** | 5 / 5 | Hệ thống bắt buộc phải tương tác với cơ sở dữ liệu và công cụ bên ngoài qua MCP Server: (1) Tool tra cứu mạng lưới tuyến đường, lộ trình, điểm dừng và thời gian hoạt động thời gian thực của xe bus điện; (2) Tool đăng ký/khởi tạo mã vé tháng và lưu vào cơ sở dữ liệu hệ thống vé VinBus. Chatbot LLM thông thường không thể tự suy diễn hoặc ghi dữ liệu vé thực tế. |
| **3. Dynamic Decision** | 4 / 5 | Hành động tiếp theo của Agent phụ thuộc hoàn toàn vào kết quả quan sát (Observation) từ bước trước: Nếu tra cứu không có tuyến chạy thẳng, Agent quyết định tìm và gợi ý tuyến trung chuyển; nếu thông tin khách hàng cung cấp còn thiếu (chưa có số điện thoại, chưa chọn điểm đón hoặc đối tượng ưu đãi), Agent quyết định hỏi thêm trước khi kích hoạt lệnh đăng ký vé; nếu mã tuyến không tồn tại, Agent thông báo lỗi lịch sự. |
| **4. Long Horizon Goal** | 4 / 5 | Agent phải theo đuổi và duy trì mục tiêu dài hạn xuyên suốt nhiều lượt tương tác: từ lúc tư vấn lộ trình di chuyển, giải đáp thắc mắc dịch vụ, đối soát dữ liệu hành khách, đến khi xuất biên nhận/mã đặt vé tháng thành công cho người dùng. |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Hãy tra cứu lộ trình và thời gian hoạt động của tuyến xe bus điện VinBus tuyến E01.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "bus_route_query",
    "arguments": {
      "route_id": "E01"
    },
    "observation": {
      "status": "SUCCESS",
      "route_id": "E01",
      "data": {
        "route_name": "Tuyến E01: Bến xe Mỹ Đình - Khu đô thị Vinhomes Ocean Park",
        "operating_hours": "05:00 - 21:00 (hằng ngày)",
        "frequency": "15 - 20 phút/chuyến",
        "ticket_price": "8.000 VNĐ/lượt",
        "stops": "Bến xe Mỹ Đình - Phạm Hùng - Khuất Duy Tiến - Nguyễn Trãi - Cầu Vĩnh Tuy - Vinhomes Ocean Park",
        "status": "Đang hoạt động"
      }
    },
    "latency_ms": 1897.37
  },
  {
    "step": 2,
    "query": "Hãy tra cứu lộ trình và thời gian hoạt động của tuyến xe bus điện VinBus tuyến E01.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "🚌 Thông tin Tuyến E01: Bến xe Mỹ Đình - Khu đô thị Vinhomes Ocean Park:\n- Giờ hoạt động: 05:00 - 21:00 (hằng ngày)\n- Tần suất: 15 - 20 phút/chuyến\n- Giá vé: 8.000 VNĐ/lượt\n- Lộ trình điểm dừng: Bến xe Mỹ Đình - Phạm Hùng - Khuất Duy Tiến - Nguyễn Trãi - Cầu Vĩnh Tuy - Vinhomes Ocean Park\n- Trạng thái: Đang hoạt động.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [v] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (OpenAI - `gpt-4o-mini`).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 / 4 lượt (TC02, TC03, TC04, TC05 gọi công cụ qua MCP Server thành công; TC01 phản hồi kiến thức chung an toàn không cần gọi Tool).
- **Kết quả đẩy Repo nộp bài:** [v] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
