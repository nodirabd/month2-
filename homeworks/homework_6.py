class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"

class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"Ульта: {self.earn()} во время полета ({self.superpower()})"

class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"Ульта: {self.viral()}, пока я свечусь ({self.live()})"

class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"Ульта: {self.earn()} благодаря тренду ({self.viral()})"


# MRO
print("Порядок поиска MRO")
print(f"GlowStreamer: {GlowStreamer.mro()}")
print(f"ViralCyborg: {ViralCyborg.mro()}")
print(f"DonateMage: {DonateMage.mro()}\n")

# live()
print(" Проверка метода live() ")
gs = GlowStreamer()
vc = ViralCyborg()

print(f"GlowStreamer.live(): {gs.live()}")
print("Сработал метод Streamer, так как он первый в списке наследования слева")

print(f"ViralCyborg.live(): {vc.live()}")
print("Сработал метод TikToker, так как он стоит перед Mutant.\n")

#Уникальные способности
print("Ultimate Content")
dm = DonateMage()
print(f"GlowStreamer: {gs.ultimate_content()}")
print(f"ViralCyborg: {vc.ultimate_content()}")
print(f"DonateMage: {dm.ultimate_content()}")