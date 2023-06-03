import pickle
import openai
import os
import json

class ChatGPT:
	def __init__(self, gpt_ver, role):
		self.gpt_ver = gpt_ver
		self.role = role
		self.history = [{"role":"system","content":"You are a "+role}]

	def generate_text(self, prompt):
		self.history.append({"role":"user","content":prompt})
		completion = openai.ChatCompletion.create(
			model=self.gpt_ver,
			max_tokens=1000,
			messages=self.history
		)
		message = completion.choices[0].message.content
		self.history.append({"role":"assistant","content":message})

		return completion.choices[0].message.content

if __name__ == "__main__":
	for file_name in os.listdir("./"):
		if file_name.endswith(".pkl"):
			with open(file_name, "rb") as file:
				gpt_a = pickle.load(file)
				with open(file_name[:-4]+".json", "w") as file:
					file.write(json.dumps(gpt_a.history, indent=2, ensure_ascii=False))
			