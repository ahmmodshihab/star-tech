# 🖥️ E-commerce Laptop Data Scraper

## 📌 Project Overview

This project is a web scraping tool built using **Python**, designed to extract laptop product data from an e-commerce website. It collects structured information such as brand, description, features, and price for analysis or further processing.

---

## 🚀 Features

* Laptop **brand name**
* Collect **product description**
* Scrape **extra features/specifications**
* Extract **price information**
* Clean and structured data output (CSV/JSON)
* Handles pagination automatically
---

## 🛠️ Tech Stack

* **Python**
* **Requests** – for sending HTTP requests
* **BeautifulSoup (bs4)** – for parsing HTML content
* **Pandas**
---

## 📂 Project Structure

```
project/
│── main.py
│── requirements.txt
│── README.md
│── data/ 
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ahmmodshihab/star-tech.git

```

### 2️⃣ Create virtual environment

```bash
conda create -p air_venv python==3.12
```

### 3️⃣ Activate environment

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

---

## 📊 Output

The scraper generates structured data including:

* Brand
* Description
* Features
* Price

Output format can be:

* CSV file
* JSON file


---

## 💡 Future Improvements

* Add support for data analysis
* Implement proxy & headers rotation
* Export to database (MySQL / MongoDB)
* Add Playwright/Selenium for dynamic sites

---

## 👨‍💻 Author

Ashfiq Ahmmod

---

## ⭐ Show Your Support

If you like this project, feel free to give it a ⭐ on GitHub!
