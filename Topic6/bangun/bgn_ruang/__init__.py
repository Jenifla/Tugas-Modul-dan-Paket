#mengimport modul yang terdapat dalam package yang sama yaitu bgn_ruang
#sehingga dapat memungkinkan menggunaan fungsi-fungsi dalam modul pada skrip utama
from . import kubus
from . import balok
from . import tabung
from . import kerucut
from . import limas
from . import prisma

#mengimport fungsi-fungsi yang ada dalam masing-masing modul
#sehingga dapat memungkinkan menggunakan fungsi-fungsi dalam modul pada skrip utama tanpa menuliskan modulnya
from .kubus import ht_kubus
from .balok import ht_balok
from .tabung import ht_tabung
from .kerucut import ht_kerucut
from .limas import ht_limas
from .prisma import ht_prisma