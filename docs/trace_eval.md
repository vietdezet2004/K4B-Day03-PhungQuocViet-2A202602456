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
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "gpa": 3.85
      }
    },
    "latency_ms": 120.5
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** ___ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** ___ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
