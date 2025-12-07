# n8n-streamlit-PPT-Generator-Web-Application

# 🌈 PPT Generator App — Streamlit + n8n + Gemini AI

A simple and powerful **AI-powered PPT Generator** that creates PowerPoint files just by using a prompt.
Built with **Streamlit** as the frontend, **n8n AI Agent + Gemini** as the backend engine, and **VS Code** for local development.

This project allows users to enter PPT details (topic, slide headings, content, etc.) → sends the request to n8n → generates PPT → returns downloadable `.pptx`.

-----

## 📸 Screenshots

### App UI
<img width="1338" height="685" alt="Interface of App using streamlit" src="https://github.com/user-attachments/assets/280ecd99-af3e-4f40-a73e-b8d25f5ab10e" />


### n8n Workflow

<img width="1470" height="956" alt="backend of PPT generator using n8n" src="https://github.com/user-attachments/assets/3863566f-2fd3-4017-90af-5be30c095412" />



---

## 🚀 Features

* Generate **PowerPoint presentations** using natural-language prompts
* Clean and responsive UI built in **Streamlit**
* Backend powered by **n8n Webhook + AI Agent (Gemini)**
* Automatically creates structured, aligned, clean PPTs
* One-click **Download PPT** button
* Works with any topic & slide structure

---

## 🧩 How It Works

1. User enters PPT details (topic, number of slides, slide content).
2. Streamlit sends the input to an **n8n Webhook**.
3. n8n AI Agent (Gemini Model) generates Python-pptx code.
4. Streamlit executes the generated Python code and builds the PPT.
5. User downloads the final `.pptx` file.

---

## 📁 Project Structure

```
.
├── app.py                                             # Streamlit frontend
├── requirements.txt                                   # Python dependencies
├── ppt generator n8n wrokflow json file.json          # n8n workflow export
├── Interface.png                                      # UI screenshot
└── Workflow.png                                       # n8n backend screenshot
```

---

## ⚙️ Installation

### 1. Install Requirements

```
pip install -r requirements.txt
```

### 2. Run Streamlit App

```
streamlit run app.py
```

### 3. n8n Setup

* Import the **ppt generator n8n wrokflow json file.json**
* Add your Gemini/OpenAI API key
* Update the Webhook URL inside `app.py`

---

## 🛠️ Tech Used

* **Streamlit**
* **n8n**
* **AI Agent (Gemini Chat Model)**
* **python-pptx**
* **VS Code**



Suggestions and improvements are welcome.
Feel free to open a PR or issue!
