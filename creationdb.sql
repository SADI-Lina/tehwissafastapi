
CREATE database tehwissa;

CREATE TABLE wilaya (
    code INT PRIMARY KEY,
    designation TEXT
);

CREATE TABLE adresse (
    id INT PRIMARY KEY AUTO_INCREMENT,
    wilaya_id INT,
    info_supp TEXT,
    FOREIGN KEY (wilaya_id) REFERENCES wilaya (code)
);

CREATE TABLE region (
    id INT PRIMARY KEY AUTO_INCREMENT,
    designation TEXT,
    adresse_id INT,
    FOREIGN KEY (adresse_id) REFERENCES adresse (id)
);

CREATE TABLE tourist_user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ntelephone INT,
    adresse_id INT,
    username VARCHAR(150),
    password VARCHAR(128),
    nom VARCHAR(30),
    prenom VARCHAR(150),
    email VARCHAR(254),
    FOREIGN KEY (adresse_id) REFERENCES adresse (id)
);

CREATE TABLE regional_user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ntelephone INT,
    region_id INT,
    username VARCHAR(150),
    password VARCHAR(128),
    nom VARCHAR(30),
    prenom VARCHAR(150),
    email VARCHAR(254),
    FOREIGN KEY (region_id) REFERENCES region (id)
);

CREATE TABLE theme (
    id INT PRIMARY KEY AUTO_INCREMENT,
    designation TEXT
);

CREATE TABLE categorie (
    id INT PRIMARY KEY AUTO_INCREMENT,
    designation TEXT
);

CREATE TABLE point_d_interet (
    id INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT,
    nom TEXT,
    nbr_visites INT DEFAULT 0,
    adresse_id INT,
    theme_id INT,
    categorie_id INT,
    FOREIGN KEY (adresse_id) REFERENCES adresse (id),
    FOREIGN KEY (theme_id) REFERENCES theme (id),
    FOREIGN KEY (categorie_id) REFERENCES categorie (id)
);


CREATE TABLE jour_choices (
    id INT PRIMARY KEY,
    label VARCHAR(50)
);

CREATE TABLE horaires_acces (
    id integer PRIMARY KEY AUTO_INCREMENT,
    heure_debut TIME NOT NULL,
    heure_fin TIME NOT NULL,
    jour_id INT NOT NULL,
    id_point_in INT NOT NULL,
    FOREIGN KEY (jour_id) REFERENCES jour_choices (id),
    FOREIGN KEY (id_point_in) REFERENCES point_d_interet (id)
);

CREATE TABLE evenement (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom TEXT,
    adresse TEXT,
    type_event TEXT,
    id_point_in INT,
    FOREIGN KEY (id_point_in) REFERENCES point_d_interet (id)
);

CREATE TABLE commentaire (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_touriste INT,
    contenu TEXT,
    nb_etoile INT,
    id_point_in INT,
    FOREIGN KEY (id_touriste) REFERENCES tourist_user (id),
    FOREIGN KEY (id_point_in) REFERENCES point_d_interet (id)
);

CREATE TABLE moyen_transport (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_pi INT,
    designation TEXT,
    FOREIGN KEY (id_pi) REFERENCES point_d_interet (id)
);
