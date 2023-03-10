PGDMP     
        
            {         
   Biblioteca    15.1    15.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    32805 
   Biblioteca    DATABASE     ?   CREATE DATABASE "Biblioteca" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Biblioteca";
                postgres    false            ?            1259    32823    Aluguel    TABLE     ?   CREATE TABLE public."Aluguel" (
    "ID" integer NOT NULL,
    "ID_Cliente" integer NOT NULL,
    "ID_Livro" integer NOT NULL,
    "Data_Aluguel" timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public."Aluguel";
       public         heap    postgres    false            ?            1259    32822    Aluguel_ID_seq    SEQUENCE     ?   ALTER TABLE public."Aluguel" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Aluguel_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    219            ?            1259    32815    Cliente    TABLE     ?   CREATE TABLE public."Cliente" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "CPF" character(11) NOT NULL
);
    DROP TABLE public."Cliente";
       public         heap    postgres    false            ?            1259    32814    Cliente_ID_seq    SEQUENCE     ?   ALTER TABLE public."Cliente" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Cliente_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    217            ?            1259    32807    Livro    TABLE     ?   CREATE TABLE public."Livro" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Autor" character varying(255) NOT NULL
);
    DROP TABLE public."Livro";
       public         heap    postgres    false            ?            1259    32806    Livro_ID_seq    SEQUENCE     ?   ALTER TABLE public."Livro" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Livro_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215                      0    32823    Aluguel 
   TABLE DATA           S   COPY public."Aluguel" ("ID", "ID_Cliente", "ID_Livro", "Data_Aluguel") FROM stdin;
    public          postgres    false    219   ?                 0    32815    Cliente 
   TABLE DATA           8   COPY public."Cliente" ("ID", "Nome", "CPF") FROM stdin;
    public          postgres    false    217          	          0    32807    Livro 
   TABLE DATA           8   COPY public."Livro" ("ID", "Nome", "Autor") FROM stdin;
    public          postgres    false    215   ?                  0    0    Aluguel_ID_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public."Aluguel_ID_seq"', 5, true);
          public          postgres    false    218                       0    0    Cliente_ID_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."Cliente_ID_seq"', 12, true);
          public          postgres    false    216                       0    0    Livro_ID_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public."Livro_ID_seq"', 10, true);
          public          postgres    false    214            w           2606    32828    Aluguel Aluguel_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT "Aluguel_pkey" PRIMARY KEY ("ID");
 B   ALTER TABLE ONLY public."Aluguel" DROP CONSTRAINT "Aluguel_pkey";
       public            postgres    false    219            s           2606    32821    Cliente Cliente_CPF_key 
   CONSTRAINT     W   ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_CPF_key" UNIQUE ("CPF");
 E   ALTER TABLE ONLY public."Cliente" DROP CONSTRAINT "Cliente_CPF_key";
       public            postgres    false    217            u           2606    32819    Cliente Cliente_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_pkey" PRIMARY KEY ("ID");
 B   ALTER TABLE ONLY public."Cliente" DROP CONSTRAINT "Cliente_pkey";
       public            postgres    false    217            q           2606    32813    Livro Livro_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."Livro"
    ADD CONSTRAINT "Livro_pkey" PRIMARY KEY ("ID");
 >   ALTER TABLE ONLY public."Livro" DROP CONSTRAINT "Livro_pkey";
       public            postgres    false    215            x           2606    32829    Aluguel fk_cliente    FK CONSTRAINT     ?   ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT fk_cliente FOREIGN KEY ("ID_Cliente") REFERENCES public."Cliente"("ID") ON DELETE CASCADE;
 >   ALTER TABLE ONLY public."Aluguel" DROP CONSTRAINT fk_cliente;
       public          postgres    false    219    3189    217            y           2606    32834    Aluguel fk_livro    FK CONSTRAINT     ?   ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT fk_livro FOREIGN KEY ("ID_Livro") REFERENCES public."Livro"("ID") ON DELETE SET NULL;
 <   ALTER TABLE ONLY public."Aluguel" DROP CONSTRAINT fk_livro;
       public          postgres    false    219    215    3185               A   x?Eʱ?0?Z??X?Hˁ<K??#??t#?	??@ꬎ?P?eI{?C#q???z?????q         {   x?E?=
?0@?Y:?OP?#E?ޥC???]5??8??!?o?C??????wޖ0??;P???'C???u
???*\??\?????&?}Rc!$:u/a???P6?݉,H>??6???"~?s"Q      	   ?   x??1J?@??z?s?i?؅<Lc0(X?L?????̮??yXYx???I??????5aK??)?4?#c?.n???ͦ~l??J??
?&?bG6??¾^???w8?3vFہ??n???#9tE???:???????P/?d??ZVhV?G?p?ZF?H?T2A;?i??V?7)K8]Ck??h????(????U???/ޯB???Q,     