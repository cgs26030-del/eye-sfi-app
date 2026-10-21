import streamlit as st

st.set_page_config(
    page_title="[빛과 눈] 학급 SFI 계산기", page_icon="👁️", layout="centered"
)

st.title("👁️ 학급 크롬북 시각 피로도(SFI) 계산기")
st.caption("모둠 [빛과 눈] | 화면 상태를 입력해 피로도를 측정해보세요.")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
  brightness = st.slider(
      "🔆 현재 화면 밝기 (%)", min_value=10, max_value=100, value=70, step=5
  )
  night_mode = st.toggle("🌙 시력보호 모드(야간 조명)", value=False)

with col2:
  time_used = st.slider(
      "⏱️ 연속 사용 시간 (분)", min_value=5, max_value=120, value=50, step=5
  )

C = 1 if night_mode else 0
sfi_score = (brightness**0.4) + (time_used**0.5) - (20 * C)

st.markdown("---")
st.subheader("📊 나의 시각 피로도 지수 (SFI)")

if sfi_score < 5:
  st.success(f"### **{sfi_score:.2f}점** - 🟢 안전 (매우 좋은 습관!)")
  st.info("💡 바른 사용 상태입니다. 이대로 유지해 주세요.")
elif sfi_score < 10:
  st.warning(f"### **{sfi_score:.2f}점** - 🟡 주의 (피로 누적 중)")
  st.write("💡 **권장:** 화면 밝기를 10~20% 낮추거나 시력보호 모드를 켜세요.")
else:
  st.error(f"### **{sfi_score:.2f}점** - 🔴 위험 (피로 고위험 상태!)")
  st.markdown("""
    **🚨 즉시 행동 수칙:**
    1. 시력보호 모드를 켜세요.
    2. 화면 밝기를 60% 이하로 내리세요.
    3. 20초 동안 창밖 먼 곳(6m 이상)을 주시하세요!
    """)
