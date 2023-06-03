import datetime
import pickle
import openai

openai.api_key = open(open("SET.INI").read()).read()

class ChatGPT:
	def __init__(self, gpt_ver, role):
		self.gpt_ver = gpt_ver
		self.role = role
		self.history = [{"role":"system","content":"You are a "+role}, {"role":"user","content":""}]

	def generate_text(self, prompt):
		completion = openai.ChatCompletion.create(
			model=self.gpt_ver,
			max_tokens=1000,
			messages=self.history[:1] + [{"role":"user","content":prompt}]
		)
		message = completion.choices[0].message.content
		self.history[1] = {"role":"assistant","content":message}
		return message

if __name__ == "__main__":
	role = input("role?:")
	gpt_ver = input("ver?(gpt-3.5-turbo/gpt-4):")
	gpt_a = ChatGPT(gpt_ver, role)

	while True:
		input_prompt = input("question？:")
		if input_prompt.lower() == 'q':
			break
		print(gpt_a.generate_text(input_prompt))
		now = datetime.datetime.now()
		str_datetime = now.strftime("%Y%m%d%H%M%S")
		file_name = str_datetime+".pkl"
		with open(file_name, "wb") as file:
			pickle.dump(gpt_a, file)
