# 📝 Info

An easy to use [Truth or Dare API](https://docs.truthordarebot.xyz/api-docs) wrapper written in [Python](https://www.python.org/).

# 💫 Main Features

- Very easy to use
- Covers entire API

# ⬇️ Installation

> **Python v3.8 or above is recommended**

```sh-session
# Windows
py -3 -m pip install truthordare.py


# Linux/macOS
python3 -m pip install truthordare.py
```

# 🔃 Import

```py
import truthordare
```

## ✅ Commands

> You can use the following Funtions :- truth() | dare() | paranoia() | wyr() | nhie()

### 👼 **Example**

```py
import truthordare

print(truthordare.truth())
print(truthordare.dare())
print(truthordare.nhie())
print(truthordare.wyr())
print(truthordare.paranoia())
```

### 🔎 With rating parameter

```py
import truthordare

print(truthordare.truth("PG"))
```

> Valid Paramaters are: - "PG" , "PG13" , "R"

## ☑️ Output Log (Example)

```sh
{'id': 'ku9abgpkwrf4', 'type': 'PARANOIA', 'rating': 'PG', 'question': "Who's most likely to enjoy reading over watching movies?", 'translations': {'bn': 'কার সিনেমা দেখার চেয়ে বেশি পড়তে ভালো লাগে?', 'de': 'Wer liest am ehest ten, anstatt sich Filme anzusehen?', 'es': '¿Quién es más probable que disfrute leyendo en lugar de ver películas?', 'fr': "Qui est le plus susceptible d'apprécier la lecture plutôt que de regarder des films\xa0?", 'hi': 'फिल्मेें देखने के बजाय पढ़ने का आनंद लेने की सबसे अधिक संभावना किसे है?', 'tl': 'Sino ang mas malamang na mag-enjoy sa pagbabasa sa panonood ng mga pelikula?'}}
```
