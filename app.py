import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="삼투압 실험 시뮬레이션", layout="centered")

st.title(" NaCl/포도당 농도에 따른 적혈구 삼투압 시뮬레이터")
st.markdown("적혈구가 어떻게 부풀거나 터지는지 시뮬레이션해보자!")
st.markdown("""
**실험 배경:**  
1학년 때 수행한 실제 실험에서, 적혈구를 다양한 농도의 포도당 및 염화나트륨(NaCl) 용액에 넣어 세포의 부피 변화와 용혈 여부를 관찰했습니다.  
이 시뮬레이터는 그 실험 데이터를 바탕으로 학습자가 간접 체험할 수 있도록 제작되었습니다.
""")

# 슬라이더 선택
solution_type = st.selectbox("용액 종류를 선택하세요", ["염화나트륨(NaCl)", "포도당(Glucose)"])

if solution_type == "염화나트륨(NaCl)":
    concentration = st.slider("NaCl 농도 (%)", 0.1, 2.0, 0.9, step=0.025)
    # 결과 도출
    if concentration < 0.45:
        state = "저장액 - 세포 팽창 후 터짐 (용혈)"
        volume = 1.3
    elif 0.45 <= concentration <= 1.2:
        state = "등장액 - 정상 상태 유지"
        volume = 1.0
    else:
        state = "고장액 - 세포 수축"
        volume = 0.7

else:  # 포도당 선택 시
    concentration = st.slider("포도당 농도 (%)", 1.0, 10.0, 5.0, step=1.0)
    if concentration < 3:
        state = "저장액 - 세포 팽창 후 터짐 (용혈)"
        volume = 1.3
    elif 3 <= concentration <= 7:
        state = "등장액 - 정상 상태 유지"
        volume = 1.0
    else:
        state = "고장액 - 세포 수축"
        volume = 0.7

# 결과 표시
st.subheader("적혈구 상태 예측")
st.write(f"선택한 {solution_type} 농도: **{concentration}%**")
st.write(f"예상되는 반응: **{state}**")
st.write(f"상대 부피 변화 (추정치): **{volume:.2f}**")

# 그래프 시각화
fig, ax = plt.subplots()
ax.bar(["RBC Volume"], [volume], color="crimson")
ax.set_ylim(0, 1.5)
ax.set_ylabel("Relative Volume (1 = normal)")
ax.set_title("Simulated Cell Volume Change")
st.pyplot(fig)
# ✅ condition 변수 정의 추가
condition = state.split(" ")[0]
# 이미지 출력
st.subheader("📸 실제 관찰 사진")
if solution_type == "염화나트륨(NaCl)":
    if condition == "저장액":
        st.image("images/rbc_actual_NaCl_0.225pct.JPG", caption="0.225% NaCl - 저장액 상태 (용혈)", use_container_width=True)
    elif condition == "등장액":
        st.image("images/rbc_actual_NaCl_0.9pct.JPG", caption="0.9% NaCl - 등장액 상태 (정상)", use_container_width=True)
    else:
        st.image("images/rbc_actual_NaCl_2pct.JPG", caption="2.0% NaCl - 고장액 상태 (수축)", use_container_width=True)
elif solution_type == "포도당(Glucose)":
    if condition == "저장액":
        st.image("images/rbc_actual_Glucose_1pct.JPG", caption="1% 포도당 - 저장액 상태 (용혈)", use_container_width=True)
    elif condition == "등장액":
        st.image("images/rbc_actual_Glucose_5pct.JPG", caption="5% 포도당 - 등장액 상태 (정상)", use_container_width=True)
    else:
        st.image("images/rbc_actual_Glucose_10pct.JPG", caption="10% 포도당 - 고장액 상태 (수축)", use_container_width=True)

# 3D 모델 이미지 출력
st.subheader("🧊 3D 모델 이미지 예시")
if condition == "저장액":
    st.image("images/rbc_model_lysed.png", caption="3D 모델 - 저장액 상태 (팽창 및 용혈)", use_container_width=True)
elif condition == "등장액":
    st.image("images/rbc_model_normal.png", caption="3D 모델 - 등장액 상태 (정상)", use_container_width=True)
else:
    st.image("images/rbc_model_shrunken.png", caption="3D 모델 - 고장액 상태 (수축)", use_container_width=True)
