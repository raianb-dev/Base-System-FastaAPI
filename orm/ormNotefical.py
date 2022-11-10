from models.modelsClient import Client, NoteFiscal
from views.notefiscalSchemas import noteficalSchemas


from sqlalchemy.orm import Session
import uuid


def add_notes(db: Session, note: noteficalSchemas):
    uuidOne = str(uuid.uuid4())
    add = NoteFiscal(
        id = uuidOne,
        clientid = note.clientId
    )
    db.add(add)
    db.commit()
    content = {
        'id': add.id
    }
    return content, 200

def get_notes(db: Session, skip: int = 0, limit: int = 20):
    query = db.query(NoteFiscal).offset(skip).limit(limit)
    data = [NoteFiscal.get() for NoteFiscal in query]
    return data, 200

def get_byId_notes(db: Session, id: str):
    # DAQUI PRA FRENTE SÓ PARA TRAZ RSRS.
    # PRECISAMOS BUSCAR PELO ID PARA FAZER O WHERE DO JOIN
    query = db.query(NoteFiscal).filter(id == id)
    # JOIN ABAIXO
    # PARA MANIPULAR O RESULTADO QUE VEM DO BANCO É
    # NESCESSÁRIO ESPERAR POR 2 OU MAIS OBJETOS DA LISTA `clientId`,`clientName` 
    # EM SEGUIDA DIZER QUAL É A POSIÇÃO EM QUE ESTÁ O ATRIBUTO ESPERADO
    # NESTE CASO É POSIÇÃO 0 `clientId`, POSIÇÃO 1 `clientName`.
    clientId, clientName = list(db.query(Client.id, Client.fullname).select_from(NoteFiscal).where(NoteFiscal.clientid == Client.id))
    # NA MODEL TEM UMA FUNÇÃO ESPERANDO POR `ClientId` E `ClientName` 
    # PODERÁ SER AJUSTADA CONFORME NESCESSÁRIO
    data = [NoteFiscal.get(clientId[0], clientName[1]) for NoteFiscal in query] 
    return data, 200

def put_notes(db: Session, note: noteficalSchemas, id: str):
    query = db.query(NoteFiscal).filter(id == id).one()
    query.clientid = note.clientId
    db.merge(query)
    db.commit()
    msg = 'updated success'
    return msg, 200

def delete_notes(db: Session, id: str):
    query = db.query(NoteFiscal).filter(id == id).one()
    db.delete(query)
    db.commit()
    msg = 'deleted success'
    return msg, 200
