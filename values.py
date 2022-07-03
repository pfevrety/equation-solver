import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
load_dotenv(".env")


class Number:
    def __init__(self, constant, variables) -> None:
        self.constant = constant
        if variables is None:
            self.variables = []
        else:
            self.variables = variables

    def __repr__(self):
        if self.constant % 1 == 0.0 and self.constant != 0.0:
            result = str(int(self.constant))
        else:
            result = str(self.constant) if self.constant != 0.0 else ''

        for variable in self.variables:
            if variable is not None:
                result += str(variable)

        if result.startswith(" + "):
            return result[3:]
        return result 

    def render(self, filename="render") -> None:
        option = webdriver.ChromeOptions()
        option.binary_location = os.environ['CHROME_PATH']
        option.add_argument("--headless") 

        browser = webdriver.Chrome(executable_path=os.environ['CHROME_DRIVER_PATH'], chrome_options=option)

        browser.get(os.environ['PROJECT_PATH'] + "generation_page/index.html?expression=" + self.generate_latex())
        element=browser.find_element(By.ID,"expression_container")
        element.screenshot(filename + ".png")

    def generate_latex(self):
        return str(self).replace(" ", "").replace("+", "è")

class Variables:
    def get_name(variables: list) -> string:
        return ''.join(variables.keys())

    def __init__(self, coef: float or int, variables: list) -> None:
        self.coef = coef
        self.variables = variables
        self.name = ''.join(sorted(variables.keys()))


    def __repr__(self) -> str:
        result = ''
        if self.coef != 0 or self.coef != 0.0:
            if self.coef == 1:
                result += ' + '
            elif self.coef == -1:
                result += ' - '
            else:
                if self.coef % 1 == 0.0:
                    result += ' + ' + str(int(self.coef)) if (self.coef >= 0) else ' - ' + str(int(self.coef)*-1)
                else:
                    result += ' + ' + str(self.coef) if (self.coef >= 0) else ' - ' + str(self.coef*-1)
            for x in self.name:
                result += f'{x}^' + str(self.variables[x]) if self.variables[x] != 1 else x
        else:
            return 
        if result == "":
            return "0"
        return result
