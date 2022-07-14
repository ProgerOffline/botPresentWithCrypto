# Телеграм хайп | Техническое задание
Телеграм бот для заработка денег, путем инвестиций пользователей.

## Клиентская часть
1. Запуск бота
2. Выбор языка
3. Кнопки
4. Мой баланс
5. Пополнить баланс 
6. Реферальная ссылка
7. Мои инвестиции
8. Вывод тела депозита
9. Техническая поддержка
10. Профиль
11. Вывод
12. Кошелек для вывода
13. Инвестиционный продукт
14. Выход
15. Дополнительно

## Маркетинг
1. Реферальная программа
2. Инвестиционный продукт

## Обозначения:
    ✅ - Сделано и протестировано.
    🔄 - В разработке.
    ⚠️ - Нехватка данных.
    📝 - Ожидает других данных.
    💢 - Присутствие багов.
    ⛔️ - Сложная реализация, возможно стоит изменить архитектуру бота.


## Клиентская часть

### Запуск бота

Когда запустили бот, выскакивает две кнопки:  Сделал одну динамичную кнопку. Если пользователь еще не зарегистрирован в боте, ему выводится кнопка “Регистрация”, если пользователь хоть раз отправил боту свой контакт он бот его автоматом регистрирует, и при следующих входах, у пользователя будет выводится кнопка “Вход”.

    ▪️Регистрация
    ▪️Войти

При нажатии кнопки показывает информационное сообщение:

    После подтверждения показывает информационное сообщение:
    💻 Welcome to your personal account. Choose language

### Выбор языка
После регистрации/авторизации человеку выскакивает 6 кнопок на выбор 

    🇺🇸 English (US)
    🇪🇸 Español (España)
    🇫🇷 Français (France)
    🇩🇪 Deutsch
    🇮🇹 Italiano
    🇻🇳 Tiếng Việt

### Кнопки
    ▪️Мой баланс
    ▪️Пополнить баланс
    ▪️Реферальная программа
    ▪️Кошелек для вывода
    ▪️Мои инвестиции
    ▪️Инвестиционный продукт
    ▪️Вывод средств
    ▪️Вывод тела депозита
    ▪️Профиль
    ▪️Поддержка
    ▪️Выход

### 1.4 Мой баланс
>При нажатии кнопки показывает информационное сообщение:
>💰 Текущий баланс: 0.00 USD

▪️Назад (на глав меню)







































1.5 Пополнить баланс

При нажатии кнопки показывает информационное сообщение:
⚖️ Выберите платежную систему для пополнения
Снизу появляются 9 кнопок

▪️Bitcoin (BTC)
▪️Ethereum (ETH)
▪️Litecoin (LTC)
▪️Bitcoin Cash (BCH)
▪️Tether (USDT TRC20)
▪️Tron (TRX)
▪️BNB (BEP2)
▪️Perfect Money (USD)
▪️Назад (на глав меню)


    
    При нажатии на любую из них показывает информационное сообщение:
💵 Введите сумму в USD
▪️Назад  (на предыдущее меню)


При вписании числа выше 100 USD показывает информационное сообщение:        💸 Чтобы пере    йти к оплате нажмите  кнопку  "Оплатить"
Снизу появятся 2 кнопки

▪️Оплатить
▪️Назад  (на глав меню)


При нажатии кнопки “Оплатить” в случае с криптой выскакивает инфо сообщение с реквизитами оплаты от коинпейменст или же ссылкой открывает. В случае с ПМ открывает окно оплаты ПМ по апи. 

После того, как клиент нажал кнопку “Оплатить” у него появятся сообщение и 1 кнопка


⏳ Ожидайте поступление денежных средств на Ваш баланс в течение часа.

▪️Назад  (на глав меню)


    
Как средства поступят приходит инфо сообщение:
    💵 Ваш баланс успешно пополнен на 1000.00 USD.
Теперь вы можете оплатить инвестиционный план в разделе “Инвестиционный продукт”


При вписании числа меньше 100 USD показывает информационное сообщение:
⚠️ Ошибка: Минимальная сумма депозита 100.00 USD
▪️Назад  (на глав меню)

1.6 Реферальная программа



Если не куплен инвестиционный план, то при нажатии кнопки показывает информационное сообщение: 
⚠️ Чтобы получить возможность получать доход от рефералов, вам необходимо приобрести инвестиционный продукт
▪️Назад  (на глав меню)


Если куплен инвестиционный план, то при нажатии кнопки показывает информационное сообщение: 
🔗 Ваша реферальная ссылка: https://t.me/
▪️Моя структура
▪️Назад  (на глав меню)


При нажатии кнопки “Моя структура” показывает инфо сообщение со всей статистикой по реферальной структуре клиента:
📈 Ваша структура
Рефералов: 1000
Активных рефералов: 500
Всего оборот: 12000.00 USD
Доход: 1800.50 USD
▪️Линия 1
▪️Линия 2
▪️Линия 3
▪️Линия 4
▪️Линия 5
▪️Линия 6
▪️Линия 6
▪️Линия 8
▪️Линия 9
▪️Линия 10
▪️Назад (на глав меню)


При нажатии любой линии показывает инфо окно по данной линии  и кнопку:
📈 Линия 1
Рефералов: 100
Активных рефералов: 25
Всего оборот: 1500.00 USD
Доход: 200.20 USD
▪️Назад (на предыдущее меню)

1.7 Кошелек для вывода

При нажатии кнопки показывает информационное сообщение и 9 кнопок:

🏦 Выберите платежную систему для вывода


▪️Tether (USDT TRC20)
▪️Perfect Money (USD)
▪️Назад (на глав меню)


После выбора платежной системы показывает инфо сообщение для ПерфектМани:
💲 Введите ваш долларовый кошелек платежной системы PerfectMoney

После выбора платежной системы показывает инфо сообщение для USDT:
💲 Введите ваш адрес USDT TRC20



При вводе кошелька в верном формате показывает информационное сообщение: 
✅ Кошелек для вывода успешно добавлен


При вводе кошелька в неверном формате показывает информационное сообщение: 
⚠️Ошибка: Неверный формат
























1.8 Мои инвестиции

При нажатии кнопки показывает информационное сообщение:
Если не сделано инвестиций
💵 Инвестиций не найдено

▪️Назад (на глав меню)



Если клиент инвестировал
💵 Инвестиционный продукт: 1000.00 USD от 07.02.2022. Всего начислено 10% / 100.00$

▪️Назад (на глав меню)




Если клиент инвестировал несколько раз
💵 Инвестиционный продукт: 1000.00 USD от 07.02.2022. Всего начислено 10% / 100.00$
💵 Инвестиционный продукт:  2500.00 USD от 12.03.2022. Всего начислено 5% / 125.00$

▪️Назад (на глав меню)



























1.9 Инвестиционный продукт

При нажатии кнопки показывает информационное сообщение:
ЕЖЕДНЕВНЫЙ ДОХОД:
🔸Апрель - 2% в день
🔸Май - 3% в день
🔸Июнь - 4% в день
🔸Июль - 5% в день
🔸Август - 6% в день

▪️Стоимость: от 100.00 USD
▪️Покупка: BTC / ETH / LTC / BCH / USDT TRC20 / TRX / BNB / Perfect Money
▪️Вывод дивидендов:  USDT TRC20 и Perfect Money (мин. сумма 10.00 USD)
▪️Время работы инвестиции: до 200% профита (ROI 300%)
▪️Вывод тела депозита: в любое время с комиссией 20%. Или без комиссии при достижении 200% прибыли.

▪️Купить
▪️Назад  (на глав меню)


При нажатии кнопки “купить” показывает информационное сообщение:
💵 Введите сумму инвестиции в USD

▪️Назад  (на глав меню)


    При вводе суммы менее 100 USD показывает информационное сообщение:
    ⚠️Ошибка: Минимальная сумма инвестиции 100.00 USD

При вводе суммы более 100 USD, но при отсутствии данной суммы на балансе показывает информационное сообщение:
    ⚠️Ошибка: На балансе недостаточно средств

При вводе суммы более 100 USD и при наличии данной суммы на балансе появляется инфо сообщение и кнопка подтверждения:
Вы совершаете покупку инвестиционного продукта на сумму 100.00 USD
▪️Подтвердить покупку
▪️Назад  (на глав меню)



После нажатия кнопки “Подтвердить покупку” средства списываются с баланса и появляется информационное сообщение:
✅ Инвестиционный продукт успешно оплачен. Каждые 24 часа вы будете получать дивиденды.

▪️Назад  (на глав меню)




1.10 Вывод средств

При нажатии кнопки показывает информационное сообщение:
🏦 Выберите платежную систему для вывода

▪️Bitcoin (BTC)
▪️Ethereum (ETH)
▪️Litecoin (LTC)
▪️Bitcoin Cash (BCH)
▪️Tether (USDT TRC20)
▪️Tron (TRX)
▪️BNB (BEP2)
▪️Perfect Money (USD)
▪️Назад (на глав меню)




Если не привязан кошелек выбранной валюты:
    ⚠️Ошибка: Добавьте BTC кошелек в разделе “Кошелек для вывода”
▪️Назад (на глав меню)


Если привязан кошелек, то после выбора платежной системы появится инфо сообщение и кнопка
💵  Введите сумму в USD
▪️Назад (на предыдущее меню)


Если на счету меньше 10 usd
⚠️Ошибка: Минимальная сумма вывода 10.00 USD
▪️Назад (на глав меню)


Если на счету больше 10 usd - появится инфо сообщение и 2 кнопки:
💳 Вы выводите 100.00 USD на ваш BTC кошелек
▪️Подтвердить
▪️Назад (на предыдущее меню)


После нажатия “Подтвердить”, если привязан кошелек Bitcoin, то:
⏳ Ожидайте поступления средств на ваш кошелек BTC. Это может занять до 24 часов.

▪️Назад (на глав меню)









1.11 Вывод тела депозита

При нажатии кнопки показывает информационное сообщение и ниже кнопки:
Выберите тело депозита инвестиционного продукта для вывода: (отображаются все инвест продукты, что купил клиент, даже если их 10)

▪️1000$
▪️2500$
▪️Назад (на глав меню)


1- если время инвест продукта не закончилось и клиент не получил 200% прибыли:
‼️ Инвестиционный период продукта не окончен. Комиссия вывода составит 20%

▪️Подтвердить
▪️Назад (на глав меню)


2- если время инвест продукта закончилось появится инфо сообщение и кнопка:
‼️ Инвестиционный период продукта окончен. Комиссия вывода составит 0%

▪️Подтвердить
▪️Назад (на глав меню)


После нажатия “Подтвердить”:
✅ Средства поступили на ваш баланс. 

▪️Назад (на глав меню)


















1.12 Профиль
При нажатии кнопки показывает информационное сообщение:
Имя: Ivan (если указано в тг)
Фамилия: Ivanov (если указано в тг)
ID: 101
ID Спонсора: 100 
Кошелек: если нету,то ⚠️ Добавьте кошелек
Кошелек PM: U12345678
Кошелек BTC: 1Bnaj482nkanNFsnfk12
Дата регистрации: 22.12.2021

▪️Назад (на глав меню)


































1.13 Техническая поддержка

При нажатии кнопки показывает информационное сообщение:
👩‍💻 По всем вопросам обращайтесь в нашу техподдержку @crptxprt 


▪️Назад (на глав меню)


    




































1.14 Выход

При нажатии кнопки показывает информационное сообщение:
🙏🏻 Спасибо, что вы с нами! Мы ждем вас снова
▪️Войти








































1.15 Дополнительно

При нажатии кнопки “Назад” в любом из разделов меню, возвращает в главный личный кабинет и показывает информационное сообщение:
🗃 Выберите раздел

Каждые 24 часа клиенту приходит информационное сообщение:
ℹ️ На ваш баланс зачислено профит в размере 25.00 USD 

После каждой покупки инвестиционного продукта рефералом приходит сообщение:
ℹ️ На ваш баланс зачислено реферальное вознаграждение в размере 100.00 USD








































2. Маркетинг
Этот тест точно нужен

2.1 Реферальная программа

Реферальная программа состоит из трех уровней:
1 уровень
6%
2 уровень
3%
3 уровень
3%
4 уровень
1%
5 уровень
0,5%
6 уровень
0,5%
7 уровень
0,5%
8 уровень
0,2%
9 уровень
0,2%
10 уровень
0,1%


Реферальная ссылка активируется только после покупки инвестиционного пакета.






















2.2 Инвестиционный продукт 

Клиенту предоставляется всего один инвестиционный план с ежедневной доходность 2% в Апреле. Затем каждый мес админ меняет на +1%. можно сразу запрограммировать на 5 мес вперед до 6%. После 5 мес на 6-7-8 итд продолжает давать 6% в день

Процент устанавливается вручную в админ-панели (если не запрограммируем автоматическую смену)

Минимальная сумма покупки инвестиционного плана - 100 долларов.


Минимальная сумма депозита на баланс в личном кабинете - 100 долларов.

Вывод дивидендов возможен в любой момент. Минимальная сумма вывода - 10 долларов.

Депозит работает до 200%. Пример, клиент инвестировал 100 долларов. Начисление будет идти пока не начислит чистыми  200% - 300 долларов. После этого прибыль перестает начисляться по данному инвест продукту.

Клиент может купить много инвест продуктов. У всех будет разное время покупки, следовательно - разное время окончания. Продукты работают отдельно друг от друга. Начисление прибыли происходит каждые 24 часа с момента покупки.

Вывод тела депозита возможен в любой момент. Комиссия 20 процентов, если период инвестиционного продукта не окончен. Если окончен - 0 процентов.


























3. Панель администрирования
ваоывлдфжаоывадлыоадло


Стандартный набор
-отображение клиентов
-заявок на оплату со статусами
-спонсоры и рефералы
-смена процента
-общая стата
-вывод ручной ПМ + Коин
-редактирование данных клиента + удаление
-возможность Массовой отправки 1. Текст сообщение в бот / 2. Картинку в бот / 3. Картинка + текст в бот


ВАЖНО:
-Пополнение баланса клиентом происходит автоматически через Коин и ПМ
-Вывод ручной



