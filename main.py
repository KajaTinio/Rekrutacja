import openai

openai.api_key = ""


def read_article(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_html_content(article_text):
    prompt = (
        "Przekształć poniższy tekst artykułu na HTML, używając odpowiednich tagów do strukturyzacji treści. "
        "Dodaj tagi <img src='image_placeholder.jpg' alt='prompt' /> tam, gdzie warto wstawić obrazy, "
        "Dodaj także podpisy pod obrazkami używając tagu <figcaption>. "
        "Nie dołączaj sekcji <html> ani <head>. Przekształć tylko treść do wstawienia między <body> i </body>.\n\n"
        f"Artykuł:\n{article_text}"
    )

    try:

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        html_content = response['choices'][0]['message']['content']
        return html_content
    except Exception as e:
        print("Wystąpił błąd:", e)
        return ""


def save_html_content(html_content, output_path="artykul.html"):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)


article_path = "Oxido.txt"


def main():

    article_text = read_article(article_path)


    html_content = generate_html_content(article_text)


    save_html_content(html_content)
    print("HTML został zapisany w pliku artykul.html")

if __name__ == "__main__":
    main()
