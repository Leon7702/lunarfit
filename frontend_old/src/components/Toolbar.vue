<template>
    <div class="toolbar">
        <!-- <button class="toolbar-button">Profil</button> -->
        <router-link to="/"><img id="houseIcon" src="@/assets/StartIcon.svg" alt="Start" /></router-link>
        <router-link to="/"><img id="calendarIcon" src="@/assets/CalendarIcon.svg" alt="Kalendar" /></router-link>
        <router-link to="/"><img id="AddIcon" src="@/assets/Add.svg" alt="Log" /></router-link>
        <router-link to="/"><img id="messageIcon" src="@/assets/ChatIcon.svg" alt="Chat" /></router-link>
        <router-link to="/"><img id="profileIcon" src="@/assets/ProfileIcon.svg" alt="Profil" /></router-link>
    </div>
</template>

<style>
router-link {
    flex: 1;
    text-decoration: none;
    color: #a3a3a3;
    font-size: 14px;
    text-align: center;
    position: relative;
}

.toolbar {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f2f2f2;
    padding: 10px;
    /* height: 60px; */
}

.toolbar-button {
    background-color: #ffffff;
    border: none;
    padding: 10px;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
}
</style>