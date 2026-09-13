"""
📚 [REFERENCE ONLY / CODE MẪU THAM KHẢO]
🧠 CẤP ĐỘ 3: NATIVE MCP AGENT (Native Tool Calling + MCP Server Integration)
⚠️ Lưu ý: File này chỉ dùng để đọc tham khảo kiến trúc. Không chỉnh sửa hay debug file này.
"""

import json

def get_weather(city: str) -> str:
    return f"Thời tiết {city}: 28°C, Nắng nhẹ."

def run_level3_demo():
    print("=== DEMO CẤP ĐỘ 3: NATIVE MCP AGENT (VINBUS) ===")
    user_goal = "Tra cứu lộ trình và điểm đón của tuyến xe bus điện VinBus E01"
    print(f"🎯 Goal: {user_goal}")
    print("🧠 [Thought]: Phát sinh Native Tool Call 'bus_route_query'...")
    print("🛠️ [Native Tool Call]: bus_route_query({'route_id': 'E01'})")
    print("👁️ [MCP Server Observation]: {'status': 'SUCCESS', 'route_id': 'E01', 'name': 'Tuyến E01: Bến xe Mỹ Đình - Vinhomes Ocean Park'}")
    print("🏁 [Final Answer]: Tuyến xe bus điện VinBus E01 xuất phát từ Bến xe Mỹ Đình đến Khu đô thị Vinhomes Ocean Park.")

if __name__ == "__main__":
    run_level3_demo()
