import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image


class QuizBandeirasApp(App):
    def build(self):
        
        self.flags = {
            "ad": "Andorra", "ae": "Emirados Árabes Unidos", "af": "Afeganistão",
            "ag": "Antígua e Barbuda", "ai": "Anguilla", "al": "Albânia",
            "am": "Armênia", "ao": "Angola", "aq": "Antártida", "ar": "Argentina",
            "as": "Samoa Americana", "at": "Áustria", "au": "Austrália",
            "aw": "Aruba", "az": "Azerbaijão",
            "ba": "Bósnia e Herzegovina", "bb": "Barbados", "bd": "Bangladesh",
            "be": "Bélgica", "bf": "Burquina Faso", "bg": "Bulgária",
            "bh": "Bahrein", "bi": "Burundi", "bj": "Benin",
            "bl": "São Bartolomeu", "bm": "Bermudas", "bn": "Brunei",
            "bo": "Bolívia", "bq": "Caribe Neerlandês", "br": "Brasil",
            "bs": "Bahamas", "bt": "Butão", "bv": "Ilha Bouvet",
            "bw": "Botsuana", "by": "Belarus", "bz": "Belize",
            "ca": "Canadá", "cd": "República Democrática do Congo",
            "cf": "República Centro-Africana", "cg": "Congo", "ch": "Suíça",
            "ci": "Costa do Marfim", "cl": "Chile",
            "cm": "Camarões", "cn": "China", "co": "Colômbia",
            "cr": "Costa Rica", "cu": "Cuba", "cv": "Cabo Verde",
            "cw": "Curaçao", "cx": "Ilha Christmas", "cy": "Chipre",
            "cz": "Tchéquia", "de": "Alemanha", "dj": "Djibouti",
            "dk": "Dinamarca", "dm": "Dominica", "do": "República Dominicana",
            "dz": "Argélia", "ec": "Equador", "ee": "Estônia",
            "eg": "Egito", "eh": "Saara Ocidental", "er": "Eritreia",
            "es": "Espanha", "et": "Etiópia", "fi": "Finlândia",
            "fj": "Fiji", "fm": "Micronésia", "fo": "Ilhas Faroe",
            "fr": "França", "ga": "Gabão", "gb": "Reino Unido",
            "gd": "Granada", "ge": "Geórgia", "gf": "Guiana Francesa",
            "gg": "Guernsey", "gh": "Gana", "gi": "Gibraltar",
            "gl": "Groenlândia", "gm": "Gâmbia", "gn": "Guiné",
            "gp": "Guadalupe", "gq": "Guiné Equatorial", "gr": "Grécia",
            "gt": "Guatemala",
            "gu": "Guam", "gw": "Guiné-Bissau", "gy": "Guiana",
            "hk": "Hong Kong", "hn": "Honduras",
            "hr": "Croácia", "ht": "Haiti", "hu": "Hungria",
            "id": "Indonésia", "ie": "Irlanda", "il": "Israel",
            "im": "Ilha de Man", "in": "Índia", "io": "Território Britânico do Oceano Índico",
            "iq": "Iraque", "ir": "Irã", "is": "Islândia",
            "it": "Itália", "je": "Jersey", "jm": "Jamaica",
            "jo": "Jordânia", "jp": "Japão", "ke": "Quênia",
            "kg": "Quirguistão", "kh": "Camboja", "ki": "Quiribati",
            "km": "Comores", "kn": "São Cristóvão e Nevis", "kp": "Coreia do Norte",
            "kr": "Coreia do Sul", "kw": "Kuwait",
            "kz": "Cazaquistão", "la": "Laos", "lb": "Líbano",
            "lc": "Santa Lúcia", "li": "Liechtenstein", "lk": "Sri Lanka",
            "lr": "Libéria", "ls": "Lesoto", "lt": "Lituânia",
            "lu": "Luxemburgo", "lv": "Letônia", "ly": "Líbia",
            "ma": "Marrocos", "mc": "Mônaco", "md": "Moldávia",
            "me": "Montenegro", "mf": "São Martinho", "mg": "Madagascar",
            "mh": "Ilhas Marshall", "mk": "Macedônia do Norte", "ml": "Mali",
            "mm": "Mianmar", "mn": "Mongólia", "mo": "Macau",
            "mq": "Martinica", "mr": "Mauritânia",
            "ms": "Montserrat", "mt": "Malta", "mu": "Maurício",
            "mv": "Maldivas", "mw": "Malawi", "mx": "México",
            "my": "Malásia", "mz": "Moçambique", "na": "Namíbia",
            "nc": "Nova Caledônia", "ne": "Níger", "nf": "Ilha Norfolk",
            "ng": "Nigéria", "ni": "Nicarágua", "nl": "Países Baixos",
            "no": "Noruega", "np": "Nepal", "nr": "Nauru",
            "nu": "Niue", "nz": "Nova Zelândia", "om": "Omã",
            "pa": "Panamá", "pe": "Peru", "pf": "Polinésia Francesa",
            "pg": "Papua Nova Guiné", "ph": "Filipinas", "pk": "Paquistão",
            "pl": "Polônia", "pm": "Saint-Pierre e Miquelon",
            "pr": "Porto Rico", "pt": "Portugal", "pw": "Palau",
            "py": "Paraguai", "qa": "Catar", "re": "Reunião",
            "ro": "Romênia", "rs": "Sérvia", "ru": "Rússia",
            "rw": "Ruanda", "sa": "Arábia Saudita", "sb": "Ilhas Salomão",
            "sc": "Seychelles", "sd": "Sudão", "se": "Suécia",
            "sg": "Singapura", "sh": "Santa Helena", "si": "Eslovênia",
            "sj": "Svalbard e Jan Mayen", "sk": "Eslováquia", "sl": "Serra Leoa",
            "sm": "San Marino", "sn": "Senegal", "so": "Somália",
            "sr": "Suriname", "ss": "Sudão do Sul", "st": "São Tomé e Príncipe",
            "sv": "El Salvador", "sx": "São Martinho", "sy": "Síria",
            "sz": "Essuatíni", "td": "Chade",
            "tf": "Terras Austrais e Antárticas Francesas", "tg": "Togo", "th": "Tailândia",
            "tj": "Tajiquistão", "tk": "Tokelau", "tl": "Timor-Leste",
            "tm": "Turcomenistão", "tn": "Tunísia", "to": "Tonga",
            "tr": "Turquia", "tt": "Trindade e Tobago", "tv": "Tuvalu",
            "tw": "Taiwan", "tz": "Tanzânia", "ua": "Ucrânia",
            "ug": "Uganda", "us": "Estados Unidos",
            "uy": "Uruguai", "uz": "Uzbequistão", "va": "Vaticano",
            "vc": "São Vicente e Granadinas", "ve": "Venezuela", 
            "vn": "Vietnã", "vu": "Vanuatu", "wf": "Wallis e Futuna",
            "ws": "Samoa", "ye": "Iêmen", "yt": "Mayotte",
            "za": "África do Sul", "zm": "Zâmbia", "zw": "Zimbábue"
        }


        self.image_dir = "bandeiras/"  # Caminho das bandeiras
        self.user_name = None  # Nome do usuário
        self.score = 0  # Pontuação
        self.current_question = 0  # Questão atual
        self.max_questions = 20  # Total de perguntas no jogo

        # Layout principal
        self.main_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Exibir nome
        self.user_name_label = Label(text="Bem-vindo! Insira seu nome para começar.", font_size=20)
        self.main_layout.add_widget(self.user_name_label)

        # Entrada de nome
        self.user_name_input = TextInput(hint_text="Digite seu nome", multiline=False, size_hint=(1, None), height=40)
        self.main_layout.add_widget(self.user_name_input)

        # Botão para salvar nome
        self.save_name_button = Button(text="Salvar Nome", size_hint=(1, None), height=50)
        self.save_name_button.bind(on_release=self.save_name)
        self.main_layout.add_widget(self.save_name_button)

        # Botão para iniciar o jogo
        self.start_game_button = Button(text="Jogar", size_hint=(1, None), height=50, disabled=True)
        self.start_game_button.bind(on_release=self.start_game)
        self.main_layout.add_widget(self.start_game_button)

        return self.main_layout

    def save_name(self, instance):
        self.user_name = self.user_name_input.text.strip()
        if self.user_name:
            self.user_name_label.text = f"Olá, {self.user_name}! Clique em 'Jogar' para começar."
            self.start_game_button.disabled = False
        else:
            self.user_name_label.text = "Por favor, insira um nome válido."

    def start_game(self, instance):
        self.score = 0
        self.current_question = 0
        self.main_layout.clear_widgets()
        self.show_question()

    def show_question(self):
        if self.current_question >= self.max_questions:
            self.show_final_score()
            return

        self.current_question += 1

        # Escolher bandeira e alternativas
        correct_country = random.choice(list(self.flags.keys()))
        correct_name = self.flags[correct_country]
        image_path = f"{self.image_dir}{correct_country}.png"

        options = [correct_name]
        while len(options) < 4:
            option = random.choice(list(self.flags.values()))
            if option not in options:
                options.append(option)
        random.shuffle(options)

        # Limpar tela e mostrar bandeira
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(Label(text=f"De que país é esta bandeira? {self.current_question}/{self.max_questions}", font_size=18))
        self.main_layout.add_widget(Image(source=image_path, size_hint=(1, 0.5), allow_stretch=True, keep_ratio=True))


        # Mostrar opções
        for option in options:
            button = Button(text=option, size_hint=(1, None), height=50)
            button.bind(on_release=lambda instance, answer=option: self.check_answer(answer, correct_name))
            self.main_layout.add_widget(button)

    def check_answer(self, selected, correct):
        if selected == correct:
            self.score += 1
        self.show_question()

    def show_final_score(self):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(Label(text=f"{self.user_name}, sua pontuação final foi: {self.score}/{self.max_questions}", font_size=24))
        restart_button = Button(text="Jogar Novamente", size_hint=(1, None), height=50)
        restart_button.bind(on_release=self.start_game)
        self.main_layout.add_widget(restart_button)


if __name__ == "__main__":
    QuizBandeirasApp().run()