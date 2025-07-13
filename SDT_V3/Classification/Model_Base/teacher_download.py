import timm
try:
    model = timm.create_model('regnety_160', pretrained=True)
    print("✅ 教师模型 'regnety_160' 加载成功！")
except Exception as e:
    print(f"❌ 教师模型加载失败: {e}")