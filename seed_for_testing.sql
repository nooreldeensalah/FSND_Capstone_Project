-- DISCLAIMER: THIS MOCK DATA WAS GENERATED WITH THE HELP OF MOCKAROO.COM
/*

      _        _
     / \   ___| |_ ___  _ __ ___
    / _ \ / __| __/ _ \| '__/ __|
   / ___ \ (__| || (_) | |  \__ \
  /_/   \_\___|\__\___/|_|  |___/


*/
BEGIN;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'gender') THEN
        CREATE TYPE gender AS ENUM ('Male', 'Female');
    END IF;
END
$$;

CREATE TABLE IF NOT EXISTS actor (
        id SERIAL NOT NULL,
        name VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        gender gender NOT NULL,
        PRIMARY KEY (id)
);

insert into Actor (name, age, gender) values ('Denny Good', 37, 'Male');
insert into Actor (name, age, gender) values ('Quincey Mahomet', 39, 'Female');
insert into Actor (name, age, gender) values ('Merrile Aaronsohn', 75, 'Male');
insert into Actor (name, age, gender) values ('Everard Winsom', 64, 'Female');
insert into Actor (name, age, gender) values ('Farlee Bragg', 18, 'Male');
insert into Actor (name, age, gender) values ('Laurene Spaight', 49, 'Male');
insert into Actor (name, age, gender) values ('Jennie Mc Ilwrick', 28, 'Male');
insert into Actor (name, age, gender) values ('Noellyn Breache', 48, 'Female');
insert into Actor (name, age, gender) values ('Gradey Cristea', 45, 'Male');
insert into Actor (name, age, gender) values ('Reginauld Kimbrough', 71, 'Male');
insert into Actor (name, age, gender) values ('Ellissa Child', 43, 'Male');
insert into Actor (name, age, gender) values ('Dahlia Savile', 54, 'Female');
insert into Actor (name, age, gender) values ('Rosetta Kienlein', 50, 'Female');
insert into Actor (name, age, gender) values ('Amie Tapscott', 40, 'Male');
insert into Actor (name, age, gender) values ('Jacqueline Kuhnke', 22, 'Male');
insert into Actor (name, age, gender) values ('Dory Delph', 67, 'Female');
insert into Actor (name, age, gender) values ('Jeno Trosdall', 35, 'Female');
insert into Actor (name, age, gender) values ('Jeana Bilfoot', 53, 'Female');
insert into Actor (name, age, gender) values ('Erma Rolfe', 20, 'Male');
insert into Actor (name, age, gender) values ('Ryley Tomson', 22, 'Male');
insert into Actor (name, age, gender) values ('Juan MacKim', 55, 'Male');
insert into Actor (name, age, gender) values ('Lindi Poulsom', 65, 'Female');
insert into Actor (name, age, gender) values ('Zola Hawkeridge', 39, 'Male');
insert into Actor (name, age, gender) values ('Torrie MacNeil', 51, 'Male');
insert into Actor (name, age, gender) values ('Damian Lowder', 22, 'Female');
insert into Actor (name, age, gender) values ('Kassandra Challender', 26, 'Female');
insert into Actor (name, age, gender) values ('Romy Brandel', 46, 'Female');
insert into Actor (name, age, gender) values ('Guillaume Aarons', 64, 'Male');
insert into Actor (name, age, gender) values ('Moise Bannell', 26, 'Male');
insert into Actor (name, age, gender) values ('Veronika Pavis', 43, 'Female');
insert into Actor (name, age, gender) values ('Griffin Fairholme', 61, 'Female');
insert into Actor (name, age, gender) values ('Crawford Easterby', 38, 'Male');
insert into Actor (name, age, gender) values ('Ricky Scougall', 55, 'Male');
insert into Actor (name, age, gender) values ('Claudina Oliveras', 35, 'Male');
insert into Actor (name, age, gender) values ('Cassandra Wallicker', 17, 'Male');
/*

   __  __            _
  |  \/  | _____   _(_) ___  ___
  | |\/| |/ _ \ \ / / |/ _ \/ __|
  | |  | | (_) \ V /| |  __/\__ \
  |_|  |_|\___/ \_/ |_|\___||___/


*/
CREATE TABLE IF NOT EXISTS movie (
        id SERIAL NOT NULL,
        title VARCHAR(100) NOT NULL,
        release_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        genre VARCHAR(80) NOT NULL,
        PRIMARY KEY (id)
);
insert into Movie (title, release_date, genre) values ('Aankhen', '3/11/1998', 'Comedy|Crime|Thriller');
insert into Movie (title, release_date, genre) values ('Prime of Miss Jean Brodie, The', '5/2/2007', 'Drama');
insert into Movie (title, release_date, genre) values ('Beyond Bedlam', '10/17/2008', 'Drama|Horror');
insert into Movie (title, release_date, genre) values ('Dr. Akagi (Kanzo sensei)', '10/21/1967', 'Comedy|Drama|War');
insert into Movie (title, release_date, genre) values ('Flying Leathernecks, The', '3/26/1978', 'Action|Drama|War');
insert into Movie (title, release_date, genre) values ('Hurlyburly', '1/1/2001', 'Drama');
insert into Movie (title, release_date, genre) values ('Megan Is Missing', '4/11/2010', 'Crime|Drama');
insert into Movie (title, release_date, genre) values ('Ricky Gervais: Out of England - The Stand-Up Special', '5/27/1973', 'Comedy');
insert into Movie (title, release_date, genre) values ('Doors, The', '7/25/2009', 'Drama');
insert into Movie (title, release_date, genre) values ('Last Stand At Saber River', '8/11/1998', 'Western');
insert into Movie (title, release_date, genre) values ('President''s Analyst, The', '11/11/2006', 'Comedy|Thriller');
insert into Movie (title, release_date, genre) values ('Dangerous Game', '5/5/1992', 'Drama');
insert into Movie (title, release_date, genre) values ('First Kid', '11/5/2018', 'Children|Comedy');
insert into Movie (title, release_date, genre) values ('U.S. Marshals', '4/10/2005', 'Action|Crime|Thriller');
insert into Movie (title, release_date, genre) values ('Terms of Endearment', '9/16/1991', 'Comedy|Drama');
insert into Movie (title, release_date, genre) values ('What Women Want', '12/7/1982', 'Comedy|Romance');
insert into Movie (title, release_date, genre) values ('How Tasty Was My Little Frenchman (Como Era Gostoso o Meu Francês)', '10/23/1974', 'Comedy|Drama');
insert into Movie (title, release_date, genre) values ('Last Laugh, The (Letzte Mann, Der)', '12/5/1998', 'Drama');
insert into Movie (title, release_date, genre) values ('Calendar', '1/5/2021', 'Drama');
insert into Movie (title, release_date, genre) values ('Winnie the Pooh and Tigger Too', '9/4/1995', 'Animation|Children');
insert into Movie (title, release_date, genre) values ('Jumpin'' Jack Flash', '7/21/1970', 'Action|Comedy|Romance|Thriller');
insert into Movie (title, release_date, genre) values ('Unsinkable Molly Brown, The', '4/5/1961', 'Musical');
insert into Movie (title, release_date, genre) values ('Things We Lost in the Fire', '1/19/2007', 'Drama|Romance');
insert into Movie (title, release_date, genre) values ('Iron Island (Jazireh Ahani)', '2/3/1981', 'Drama');
insert into Movie (title, release_date, genre) values ('Batman/Superman Movie, The', '10/27/1975', 'Action|Adventure|Animation|Children|Fantasy|Sci-Fi');
insert into Movie (title, release_date, genre) values ('Rocket Gibraltar', '4/9/2014', 'Drama');
insert into Movie (title, release_date, genre) values ('King of Masks, The (Bian Lian)', '12/9/2010', 'Drama');
insert into Movie (title, release_date, genre) values ('Anastasia', '9/14/1986', 'Drama');
insert into Movie (title, release_date, genre) values ('Con Air', '3/10/1976', 'Action|Adventure|Thriller');
insert into Movie (title, release_date, genre) values ('Oh, God!', '4/30/2006', 'Comedy|Fantasy');
insert into Movie (title, release_date, genre) values ('Quest for Fire (Guerre du feu, La)', '7/20/2013', 'Adventure|Drama');
insert into Movie (title, release_date, genre) values ('Candyman 3: Day of the Dead', '12/21/2016', 'Horror');
insert into Movie (title, release_date, genre) values ('Sarraounia', '10/11/1985', 'Drama|War');
insert into Movie (title, release_date, genre) values ('The Scapegoat', '12/2/1960', 'Drama');
insert into Movie (title, release_date, genre) values ('The Italian Connection', '10/26/1977', 'Crime|Drama');
/*

                        _                    _
   _ __ ___   _____   _(_) ___     __ _  ___| |_ ___  _ __
  | '_ ` _ \ / _ \ \ / / |/ _ \   / _` |/ __| __/ _ \| '__|
  | | | | | | (_) \ V /| |  __/  | (_| | (__| || (_) | |
  |_| |_| |_|\___/ \_/ |_|\___|___\__,_|\___|\__\___/|_|
                             |_____|

*/
CREATE TABLE IF NOT EXISTS movie_actor (
        movie_id INTEGER NOT NULL,
        actor_id INTEGER NOT NULL,
        PRIMARY KEY (movie_id, actor_id),
        FOREIGN KEY(movie_id) REFERENCES movie (id),
        FOREIGN KEY(actor_id) REFERENCES actor (id)
);

insert into movie_actor (movie_id, actor_id) values (32, 35);
insert into movie_actor (movie_id, actor_id) values (3, 19);
insert into movie_actor (movie_id, actor_id) values (14, 23);
insert into movie_actor (movie_id, actor_id) values (18, 20);
insert into movie_actor (movie_id, actor_id) values (14, 1);
insert into movie_actor (movie_id, actor_id) values (31, 5);
insert into movie_actor (movie_id, actor_id) values (27, 30);
insert into movie_actor (movie_id, actor_id) values (31, 7);
insert into movie_actor (movie_id, actor_id) values (22, 35);
insert into movie_actor (movie_id, actor_id) values (28, 26);
insert into movie_actor (movie_id, actor_id) values (26, 7);
insert into movie_actor (movie_id, actor_id) values (31, 8);
insert into movie_actor (movie_id, actor_id) values (30, 17);
insert into movie_actor (movie_id, actor_id) values (26, 23);
insert into movie_actor (movie_id, actor_id) values (21, 8);
insert into movie_actor (movie_id, actor_id) values (24, 3);
insert into movie_actor (movie_id, actor_id) values (4, 31);
insert into movie_actor (movie_id, actor_id) values (35, 33);
insert into movie_actor (movie_id, actor_id) values (15, 20);
insert into movie_actor (movie_id, actor_id) values (6, 32);
insert into movie_actor (movie_id, actor_id) values (14, 16);
insert into movie_actor (movie_id, actor_id) values (14, 25);
insert into movie_actor (movie_id, actor_id) values (15, 13);
insert into movie_actor (movie_id, actor_id) values (12, 6);
insert into movie_actor (movie_id, actor_id) values (17, 2);
insert into movie_actor (movie_id, actor_id) values (19, 26);
insert into movie_actor (movie_id, actor_id) values (33, 22);
insert into movie_actor (movie_id, actor_id) values (4, 9);
insert into movie_actor (movie_id, actor_id) values (18, 10);
insert into movie_actor (movie_id, actor_id) values (34, 25);
insert into movie_actor (movie_id, actor_id) values (16, 15);
insert into movie_actor (movie_id, actor_id) values (29, 22);
insert into movie_actor (movie_id, actor_id) values (17, 4);
insert into movie_actor (movie_id, actor_id) values (24, 34);
insert into movie_actor (movie_id, actor_id) values (14, 7);


COMMIT;