j = 2

for i in range(0,9):
    j = 2*i
    print(i,j)

k = 2
j = 1
i = 0

# Ladeni (IDLE!!):
# - v hlavnim okne IDLE: menu Debug -> Debugger (otevre okno debuggeru)
# - obvykle vhodne zatrhnout checkbox Source (oznacovat aktualni prikaz -
#   sedy pruh). Pripadne zatrhnout i Globals
# - v okne ladeneho programu: prava mys na radku, kde chci zastavit ->
#   Set Breakpoint (zluty pruh)
# - v okne ladeneho programu spustit: Run -> Run Module

# Tlacitky v okne debuggeru lze krokovat (Step), spoustet (Go), prohlizet
# promenne atd.
# Tlacitko Over - projet volane funkce plnou rychlosti krokovat az po
# navratu.
# Tlacitko Out - danou funkci (a v ni dalsi volani) projet plnou rychlosti
# a krokovat az po navratu z ni.

# Po spusteni programu v debuggeru se AUTOMATICKY program zastavi na
# prvnim radku!!
