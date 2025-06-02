from tkinter import *
from tkinter import messagebox
from api_handler import fetch_exchange_data
from logic import find_currency_rate, calculate

# GUI 윈도우 설정
window = Tk()
window.title("환율 계산기")
window.geometry("400x450")
window.resizable(width=False, height=False)

# 통화 코드 리스트
currency_codes = [
    "USD (미국 달러)", "JPY (일본 엔)", "EUR (유로)", "CNY (중국 위안)",
    "HKD (홍콩 달러)", "GBP (영국 파운드)", "AUD (호주 달러)",
    "CAD (캐나다 달러)", "CHF (스위스 프랑)", "SGD (싱가포르 달러)"
]

# 통화 코드 보기 라벨
Label(window, text="☑️ 환전 가능한 통화 코드 <보기>:", fg="blue").pack(pady=(10, 0))
Label(window, text=", ".join(currency_codes), wraplength=380, justify=LEFT).pack(pady=(0, 10))

# 통화 코드 입력
Label(window, text="환전할 통화 코드 (예: USD, JPY):").pack()
currency_entry = Entry(window, width=20)
currency_entry.pack()

# 변환 방향 선택
Label(window, text="변환 방향 선택: 1 (원화→외화), 2 (외화→원화)").pack()
direction_var = StringVar()
direction_entry = Entry(window, width=5, textvariable=direction_var)
direction_entry.pack()

# 금액 입력
Label(window, text="환전할 금액 입력:").pack()
amount_entry = Entry(window, width=20)
amount_entry.pack()

# 결과 출력
result_label = Label(window, text="", fg="green", font=("Arial", 12))
result_label.pack(pady=10)

# 계산 버튼 기능
def on_calculate():
    try:
        currency = currency_entry.get().upper().strip()
        direction = direction_var.get().strip()
        amount = float(amount_entry.get().strip())

        rate_data = fetch_exchange_data()
        rate = find_currency_rate(rate_data, currency)

        if rate is None:
            messagebox.showerror("오류", "해당 통화 코드를 찾을 수 없습니다.")
            return

        result = calculate(amount, rate, direction)
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("입력 오류", "금액을 숫자로 입력해주세요.")
    except Exception as e:
        messagebox.showerror("오류", f"예기치 못한 오류 발생: {e}")

# 버튼
Button(window, text="환율 계산", command=on_calculate).pack(pady=10)

# 실행
window.mainloop()
