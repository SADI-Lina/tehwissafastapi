from pydantic import BaseModel

class CommentaireBase(BaseModel):
    id_touriste: int
    contenu: str
    nb_etoile: int
    id_point_in: int

class CommentaireCreate(CommentaireBase):
    pass

class Commentaire(CommentaireBase):
    id: int

    class Config:
        orm_mode = True