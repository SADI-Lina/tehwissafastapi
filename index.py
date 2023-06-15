from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import point_d_interet , adresse , theme , categorie , moyen_transport , evenement,type_event
from config.db import engine

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the point router
app.include_router(point_d_interet.router)
app.include_router(adresse.router)
app.include_router(theme.router)
app.include_router(categorie.router)
app.include_router(moyen_transport.router)
app.include_router(evenement.router)
app.include_router(type_event.router)

#app.include_router(horaires_acces.router)

# Create the database tables
from models.point_d_interet import Base
from models.adresse import Base
from models.theme import Base
from models.categorie import Base
#from models.horaires_acces import Base
from models.moyen_transport import Base
from models.evenement import Base
from models.type_event import Base

Base.metadata.create_all(bind=engine)