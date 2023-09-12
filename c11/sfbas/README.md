# sfbas - StaticFoolBasic

* Что: ещё одна реализация BASIC
* Зачем: упрощение жизни "новичкам", практика в программировании парсеров/лексеров/ЯПов
* Язык: Си (стандарт 11, использует CMake+Make/Ninja/VS), SFB

> **Предупреждение**: исходный код sfbas находится [**здесь**](https://github.com/steet-polezhaev-unoff/sfbas).

sfbas - появившаяся по многим причинам реализация BASIC. Она вдохновлена QBasic и Visual Basic.

BASIC преподают как язык "для самых дубов в программировании" (ровно как и Python). Отчасти, так и должно быть, но он успел раз так двадцать устареть, как и методики его преподавания. По этой причине проискодит непонимание того, как на нём писать (да-да, именно так). И хоть это "язык для начинающих", он не совсем "многозадачен" (например, мне бы хотелось видеть систему модулей, собственных типов данных, взаимодействие с Си и, что немаловажно, кроссплатформенность).

На момент появления идеи я также начинал практику в парсинге исходных текстов с помощью RegExp и перевод результата в АСД. "Искра, буря, взрыв", и репозиторий sfbas создан.