# Project: EDA кредитного риска (Alfa Bank PD Credit History)

Учебный проект в рамках лабораторной №1 «Инициация проекта».

## Описание

Разведочный анализ данных (EDA) временного ряда кредитного риска на основе набора Alfa Bank PD Credit History.  
Цель — построить воспроизводимый EDA-пайплайн: описательная статистика, визуализация, диагностика выбросов, обработка пропусков и обогащение признаками.

## Цель

Построить воспроизводимый EDA-пайплайн для временного ряда доли дефолтов, который помогает выявлять ранние сигналы ухудшения качества кредитного портфеля.

## Ключевые функции

- Загрузка и первичная очистка данных Alfa Bank PD Credit History.
- Описательная статистика по 11 содержательным переменным.
- Визуализация: динамика доли дефолтов, гистограмма, ACF/PACF, сезонный график.
- Диагностика выбросов (правило 1,5×IQR, z-оценки).
- Обработка пропусков линейной интерполяцией.
- Обогащение признаками: Lag1, Lag2, MA(3).

## Wiki

- [Home](https://github.com/elizabet24/project/wiki/Home)
- [Ideas](https://github.com/elizabet24/project/wiki/Ideas)
- [Evaluation](https://github.com/elizabet24/project/wiki/Evaluation)
- [Concept](https://github.com/elizabet24/project/wiki/Concept)
- [Stakeholders](https://github.com/elizabet24/project/wiki/Stakeholders)

## Эксперты

- Лобанова Е.С. (менеджер проекта)
- Преподаватель: Богушов А.К.
- Эксперт 1: Лобанова Е.С.
- Эксперт 2: Нуреева С.Р.

## Структура репозитория
- `data/` — данные
  - `raw/` — исходные (не хранятся в репо)
  - `processed/` — обработанные
- `notebooks/` — Jupyter-ноутбуки с EDA
- `src/` — Python-скрипты
- `docs/` — методология и документация
- `reports/` — итоговые отчёты
- `LICENSE` — лицензия MIT
- `.gitignore` — исключения Git
- `README.md` — описание проекта

## Источник данных

Alfa Bank PD Credit History — Kaggle:  
https://www.kaggle.com/competitions/alfa-bank-pd-credit-history
