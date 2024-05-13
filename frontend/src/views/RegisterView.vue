<template>
    <header>
        <img alt="Lunafit logo" class="logo" src="@/assets/LunaFit.png" height="45" />
    </header>
    <div>
        <form @submit="submitForm">
            <div class="input-icon">
                <img class="left-icon" src="@/assets/Communication.svg" alt="Email Icon" />
                <input type="email" id="email" v-model="email" placeholder="E-Mail" required>
            </div>

            <div class="input-icon">
                <img class="left-icon" src="@/assets/System.svg" alt="Password Icon" />
                <input type="password" id="password" v-model="password" placeholder="Passwort" required>
                <img class="right-icon" src="@/assets//Non-categorized.svg" alt="Eye closed Icon" />
            </div>

            <div class="input-icon">
                <img class="left-icon" src="@/assets//System.svg" alt="Password Icon" />
                <input type="password" id="confirmPassword" v-model="confirmPassword" placeholder="Passwort bestätigen"
                    required>
                <img class="right-icon" src="@/assets//Non-categorized.svg" alt="Eye closed Icon" />
            </div>

            <button type="submit">Registrieren</button>
        </form>
    </div>
    <p style="text-align: center;">
        Du hast einen Account?
        <a href="/login">Jetzt anmelden</a>
    </p>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            email: '',
            password: ''
        };
    },
    methods: {
        register() {
            // Hier kannst du den Registrierungsprozess implementieren
            // Zum Beispiel: eine API-Anfrage an den Server senden
            console.log('Registrierung abgeschickt');
        }
    }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');

header {
    line-height: 1.5;
}

body {
    margin: 0;
    line-height: normal;
}

h1 {
    font-weight: 500;
    font-size: 2.6rem;
    position: relative;
    top: -10px;
}

h3 {
    font-size: 1.2rem;
}

input {
    display: block;
    margin-bottom: 10px;
    width: 100%;
    padding: 10px;
    font-size: 16px;
}

button {
    position: relative;
    border-radius: 36px;
    background-color: #50c1ba;
    width: 80%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 10px 60px;
    margin: 50px auto;
    /* Add 'auto' to center the button horizontally */
    box-sizing: border-box;
    cursor: pointer;
    text-align: center;
    font-size: 20px;
    color: #fff;
    font-family: Inter;
    border: none;
    /* Add this line to remove the gray border */
}

p {
    font-size: 14px;
}

a {
    color: #50c1ba;
    font-weight: bold;
    font-size: 14px;
}

.logo {
    display: block;
    margin: 4rem auto 8rem;
}

.input-icon {
    position: relative;
}

/*
.input-icon>img {
    position: absolute;
    left: 10px;
    top: 10px;
    width: 26px;
    height: 26px;
} 
*/

.input-icon>.left-icon {
    position: absolute;
    left: 10px;
    top: 50%;
    transform: translateY(-50%);
    width: 26px;
    /* Adjust as needed */
    height: 26px;
    /* Adjust as needed */
}

.input-icon>.right-icon {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    width: 26px;
    /* Adjust as needed */
    height: 26px;
    /* Adjust as needed */
}

.input-icon>input {
    width: 100%;
    border: 1px solid #ececec;
    box-sizing: border-box;
    padding-left: 30px;
    height: 47px;
}

::placeholder {
    color: #959595;
    padding-left: 20px;
    opacity: 1;
    position: relative;
    font-size: 16px;
    font-family: Inter;
}

@media (min-width: 1024px) {
    header {
        display: flex;
        place-items: center;
        padding-right: calc(var(--section-gap) / 2);
    }

    .logo {
        margin: 0 2rem 0 0;
    }

    header .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
    }
}
</style>