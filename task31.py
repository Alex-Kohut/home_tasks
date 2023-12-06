def clean_html(input_file, output_file="draft.html"):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            html_content = file.read()


            clean_text = ''
            inside_tag = False
            for char in html_content:
                if char == '<':
                    inside_tag = True
                elif char == '>':
                    inside_tag = False
                elif not inside_tag:
                    clean_text += char


            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(clean_text)

            print(f"Очищений текст збережено у файлі {output_file}")

    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


clean_html("draft.html")