while (1) {
    /* Espera a ser despertado */
    wait(santa_sem);

    wait(mutex);

    /* Todos los renos preparados? */
    if (renos == TOTAL_RENOS) {
        prepararTrineo();
        /* Notificar a los renos... */
        for (i = 0; i < TOTAL_RENOS; i++)
            signal(renos_sem);
    }
    else if (duendes == NUM_DUENDES_GRUPO) {
        ayudarDuendes();
        /* Notificar a los duendes... */
        for (i = 0; i < NUM_DUENDES_GRUPO; i++)
            signal(duendes_sem);
    }

    signal(mutex);
}