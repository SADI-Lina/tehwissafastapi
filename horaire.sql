/*CREATE TABLE horaires_acces (
    id integer PRIMARY KEY AUTO_INCREMENT,
    heure_debut TIME NOT NULL,
    heure_fin TIME NOT NULL,
    jour_id INT NOT NULL,
    FOREIGN KEY (jour_id) REFERENCES jour_choices (id)
);*/

delete from point_d_interet;

alter table point_d_interet
add column Dimanche text,
add column Lundi text,
add column Mardi text,
add column Mercredi text,
add column Jeudi text,
add column Vendredi text,
add column Samedi text;


INSERT INTO point_d_interet (description, nom, nbr_visites, adresse_id, theme_id, categorie_id , Dimanche , Lundi , Mardi , Mercredi, Jeudi, Vendredi, Samedi)
VALUES
    ('Le magnifique parc national de Tlemcen.', 'Parc national de Tlemcen', 0, (SELECT id FROM adresse WHERE wilaya_id = 13 LIMIT 1), 2, 2 , "De 09:00 à 19:00", "De 09:00 à 19:00", "De 09:00 à 19:00", "De 09:00 à 19:00","De 09:00 à 19:00","Fermé" , "Fermé"),
    ('La célèbre mosquée de Tlemcen.', 'Mosquée Sidi Boumediene', 0, (SELECT id FROM adresse WHERE wilaya_id = 13 LIMIT 1), 1, 1,"De 09:00 à 19:00", "De 09:00 à 19:00", "De 09:00 à 19:00", "De 09:00 à 19:00","De 09:00 à 19:00","Fermé" , "Fermé"),
    ('Une magnifique plage à Tlemcen.', 'Plage Les Andalouses', 0, (SELECT id FROM adresse WHERE wilaya_id = 13 LIMIT 1), 3, 4,"De 09:00 à 19:00", "De 09:00 à 19:00", "De 09:00 à 19:00", "De 09:00 à 19:00","De 09:00 à 19:00","Fermé" , "Fermé");
