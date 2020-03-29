# class TextInfillingModel(object):




batch = ["twinkle twinkle [MASK] star", "Happy birthday to [MASK]", "the answer to life",
             "the [MASK], and everything"];
model = TextInfillingModel()
outputs = model.predict(batch)
print(outputs)
