import random
from datetime import datetime, timedelta, timezone

import streamlit as st

# ---------- 운세 재료 ----------
ZODIAC = {
    "쥐띠": "🐭", "소띠": "🐮", "호랑이띠": "🐯", "토끼띠": "🐰",
    "용띠": "🐲", "뱀띠": "🐍", "말띠": "🐴", "양띠": "🐑",
    "원숭이띠": "🐵", "닭띠": "🐔", "개띠": "🐶", "돼지띠": "🐷",
}

TOTAL = [
    "생각지 못한 곳에서 기쁜 소식이 들려오는 하루예요.",
    "서두르기보다 한 박자 쉬어 가면 일이 술술 풀려요.",
    "주변 사람의 작은 도움이 큰 힘이 되는 날이에요.",
    "미뤄 두었던 일을 시작하기 딱 좋은 날이에요.",
    "말 한마디가 복을 부르니 고운 말을 써 보세요.",
    "오늘은 욕심을 덜어 낼수록 마음이 가벼워져요.",
    "새로운 사람과의 만남이 좋은 인연으로 이어져요.",
    "작은 실수도 웃어넘기면 금세 지나가는 하루예요.",
]
MONEY = [
    "지갑을 단단히! 충동구매만 조심하면 괜찮아요.",
    "뜻밖의 작은 수입이 생길 수 있어요.",
    "계획한 만큼만 쓰면 넉넉한 하루예요.",
    "누군가에게 베푼 만큼 돌아오는 날이에요.",
]
HEALTH = [
    "물을 자주 마시면 컨디션이 좋아져요.",
    "가벼운 스트레칭으로 몸을 풀어 주세요.",
    "오늘은 일찍 잠자리에 드는 게 보약이에요.",
    "점심 후 짧은 산책이 기운을 북돋아 줘요.",
]
COLORS = ["빨강", "주황", "노랑", "초록", "파랑", "보라", "하양", "분홍"]


def today_korea():
    """한국 시간 기준 오늘 날짜 (서버가 외국에 있어도 맞게)"""
    return datetime.now(timezone(timedelta(hours=9))).date()


def get_fortune(animal, day):
    # 같은 날, 같은 띠면 몇 번을 눌러도 같은 운세가 나오도록 함
    rng = random.Random(f"{day}-{animal}")
    return {
        "total": rng.choice(TOTAL),
        "money": rng.choice(MONEY),
        "health": rng.choice(HEALTH),
        "stars": rng.randint(2, 5),
        "color": rng.choice(COLORS),
        "number": rng.randint(1, 45),
    }


# ---------- 화면 ----------
st.title("🔮 오늘의 운세")
today = today_korea()
st.write(f"**{today.year}년 {today.month}월 {today.day}일**, 띠를 고르면 오늘의 운세를 알려 드려요.")

animal = st.selectbox("나의 띠를 선택하세요", list(ZODIAC.keys()))

if st.button("운세 보기"):
    f = get_fortune(animal, today)
    st.header(f"{ZODIAC[animal]} {animal}의 오늘")
    st.write("**총운** " + "⭐" * f["stars"] + "☆" * (5 - f["stars"]))
    st.info(f["total"])
    st.write(f"💰 **금전운** {f['money']}")
    st.write(f"💪 **건강운** {f['health']}")
    st.write(f"🎨 **행운의 색** {f['color']}  |  🔢 **행운의 숫자** {f['number']}")
