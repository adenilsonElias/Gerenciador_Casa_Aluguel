import api 

conn = api.make_connection()
inqs = api.PagamentoDAO(conn)

print(inqs.realiza_pagamento('1','1', '1', False))
print(inqs.realiza_pagamento('2','2', '2', False, True))
print(inqs.realiza_pagamento('3','3', '3', False))
print(inqs.realiza_pagamento('3','3', '3', False, rollback=True))
print(inqs.realiza_pagamento('4','4', '4', False, True))
print(inqs.realiza_pagamento('5','5', '5', False))
conn.commit()


