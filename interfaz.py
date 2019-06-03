from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


from hashmap import Hash
from colaPrioridad import Cola
from hashmap import Persona


class AgregarPersona(GridLayout):

    def __init__(self, **kwargs):
        super(AgregarPersona, self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text = "Nombre del paciente"))
        self.tiNombrePa = TextInput(hint_text = 'Nombre', multiline=False)
        self.add_widget(self.tiNombrePa)

        self.add_widget(Label(text = "Edad"))
        self.tiEdad = TextInput(hint_text = 'Edad', multiline=False)
        self.add_widget(self.tiEdad)

        self.add_widget(Label(text = "Altura"))
        self.tiAltura = TextInput(hint_text = 'Altura', multiline=False)
        self.add_widget(self.tiAltura)

        self.add_widget(Label(text = "Peso"))
        self.tiPeso = TextInput(hint_text = 'Peso', multiline=False)
        self.add_widget(self.tiPeso)

        self.add_widget(Label(text = "Tipo de Sangre"))
        self.tiTipoS = TextInput(hint_text = 'Tipo de sangre', multiline=False)
        self.add_widget(self.tiTipoS)

        self.add_widget(Label(text = "Alergias"))
        self.tiAlergias = TextInput(hint_text = 'Alergias', multiline=False)
        self.add_widget(self.tiAlergias)

        self.add_widget(Label(text = "Sintomas"))
        self.tiSintomas = TextInput(hint_text = 'Sintomas', multiline=False)
        self.add_widget(self.tiSintomas)

        self.add_widget(Label(text = "Gravedad"))
        self.tiGravedad = TextInput(hint_text = 'Gravedad entre 1-10', multiline=False)
        self.add_widget(self.tiGravedad)


        self.add_widget(Button(text='Agregar persona', on_press= self.generarPersona))
        self.add_widget(Button(text='Cancelar', on_press = self.noAgregar))

    def generarPersona(self, instance):
        if self.tiNombrePa.text == "" or self.tiAlergias.text == "" or self.tiAltura.text == "" or self.tiEdad.text == "" or self.tiGravedad.text == "" or self.tiPeso.text == "" or self.tiSintomas.text == "" or self.tiTipoS.text == "":
            popup = Popup(title='Alerta!',content=Label(text='Rellenar todos los campos!'),size_hint=(None, None), size=(300, 100))
            popup.open()
        else:
            temp = Persona(self.tiNombrePa.text, self.tiEdad.text, self.tiAltura.text, self.tiPeso.text, self.tiTipoS.text, self.tiAltura.text, self.tiSintomas.text)
            prioridad = int(self.tiGravedad.text)
            dat.NumeroPacientes+=1
            sm.current = 'principal'
            if(dat.NumeroDoctores>=dat.NumeroPacientes):
                prin.add_widget(ModuloPaciente(temp))
            else:
                dat.col.insert(temp,prioridad)
            self.tiAlergias.text=''
            self.tiAltura.text=''
            self.tiEdad.text=''
            self.tiGravedad.text=''
            self.tiNombrePa.text=''
            self.tiPeso.text=''
            self.tiSintomas.text=''
            self.tiTipoS.text=''
    def noAgregar(self,instance):
        self.tiAlergias.text=''
        self.tiAltura.text=''
        self.tiEdad.text=''
        self.tiGravedad.text=''
        self.tiNombrePa.text=''
        self.tiPeso.text=''
        self.tiSintomas.text=''
        self.tiTipoS.text=''
        sm.current='principal'

class Botones(GridLayout):
    def __init__(self,**kwargs):
        
        super(Botones, self).__init__(**kwargs)
        self.cols=5
        self.add_widget(Button(text='Agregar Persona', on_press=self.agregarPersonaMenu))
        self.add_widget(Button(text='Agregar Doctor', on_press = self.incrementarDoctor))
        self.lNum= Label(text='Numero doctores: ' + str(dat.NumeroDoctores))
        self.add_widget(self.lNum)
        self.add_widget(Button(text='Quitar Doctor', on_press = self.disminuirDoctor))
        self.add_widget(Button(text='Consultar paciente', on_press = self.consult))


    def consult(self, instance):
        sm.current = 'consultar'


    def incrementarDoctor(self, instance):
        dat.NumeroDoctores+=1
        self.lNum.text = 'Numero doctores: ' + str(dat.NumeroDoctores)
        if(not dat.col.isEmpty()):
            temp = dat.col.pop()
            prin.add_widget(ModuloPaciente(temp))

    def disminuirDoctor(self, instance):
        if(dat.NumeroDoctores == 0):
            pop= Popup(title='Alerta!', content=Label(text = "No se pueden disminuir mas doctores"),size_hint=(None, None), size=(500, 300))
            pop.open()
        else:
            dat.NumeroDoctores-=1
            self.lNum.text = 'Numero doctores: ' + str(dat.NumeroDoctores)

    def agregarPersonaMenu(self,instance):
        sm.current='agregar'



def consultarPersona(p):
    datos = "Nombre: " + p.nombre + "\nEdad: " + p.edad + "\nAltura: " + p.altura + "\nPeso: " + p.peso + "\nTipo de Sangre: " + p.tipoS + "\nAlergias: "+ p.alergias + "\nSintomas: " + p.sintomas
    popup = Popup(title='Datos', content=Label(text = datos),size_hint=(None, None), size=(500, 300))
    popup.open()

class Principal(GridLayout):
    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.cols=1
        self.add_widget(Botones())
        
    
class ConsultarHash(GridLayout):
    def __init__(self, **kwargs):
        super(ConsultarHash, self).__init__(**kwargs)
        self.cols = 2

        self.nombre = TextInput(hint_text = 'Nombre completo del paciente', multiline=False)
        self.add_widget(self.nombre)
        self.add_widget(Button(text='Consultar',on_press= self.con))
        self.add_widget(Button(text='Regresar', on_press = self.regresar))

    def con(self, instance):
        a = self.nombre.text
        temp = dat.hash.search(a)
        if(temp == None):
            popup = Popup(title='Alerta!', content=Label(text = "No se encontro la informacion"),size_hint=(None, None), size=(500, 300))
        else:
            consultarPersona(temp)
    def regresar(self,instance):
        sm.current = 'principal'



class ModuloPaciente(GridLayout):
    def __init__(self,a,**kwargs):
        
        super(ModuloPaciente, self).__init__(**kwargs)
        self.persona = a
        self.cols = 4
        self.add_widget(Label(text="Paciente: " + a.nombre))
        self.add_widget(Label(text='Estado'))
        self.add_widget(Button(text='Informacion', on_press=self.inforPersona))
        self.add_widget(Button(text='Listo', on_press = self.terminarPersona))

    def inforPersona(self,instance):
        consultarPersona(self.persona)
    def terminarPersona(self,instance):
        prin.remove_widget(self)
        dat.hash.insert(self.persona)
        dat.NumeroPacientes-=1
        if not dat.col.isEmpty() and dat.NumeroDoctores >= dat.NumeroPacientes:
            temp = dat.col.pop()
            prin.add_widget(ModuloPaciente(temp))
            

class MyApp(App):

    def build(self):
        return sm

class Datos(object):
    def __init__(self):
        self.NumeroPacientes= 0
        self.NumeroDoctores = 0
        self.col = Cola()
        self.hash = Hash()


if __name__ == '__main__':
    a = Persona("","","","","","","")
    

    dat = Datos()

    sm = ScreenManager()
    prin = Principal()
    screen1 = Screen(name = 'principal')
    screen1.add_widget(prin)
    sm.add_widget(screen1)

    screen2 = Screen(name = 'agregar')
    screen2.add_widget(AgregarPersona())
    sm.add_widget(screen2)

    screen3 = Screen(name = 'consultar')
    a = ConsultarHash()
    screen3.add_widget(a)
    sm.add_widget(screen3)

    sm.current = 'principal'

    MyApp().run()