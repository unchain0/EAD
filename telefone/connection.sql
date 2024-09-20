CREATE TABLE public."AGENDA"
    (
        id integer NOT NULL,
        nome text COLLATE pg_catalog."default" NOT NULL,
        telefone char(12) COLLATE pg_catalog."default" NOT NULL
    )
TABLESPACE pg_default;

ALTER TABLE public."AGENDA"
    OWNER TO postgres;

INSERT INTO public."AGENDA"(id, nome, telefone)
VALUES (1, 'teste 1', '021999999999');

SELECT *
  FROM public."AGENDA";