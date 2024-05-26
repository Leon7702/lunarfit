<template>
    <div class="arrow-down-sign-to">
      <img class="path" alt="Path" src="lunarfit/frontend/src/assets/arrow-left.svg" />
    </div>
  </template>
  
  <script>
  export default {
    name: "ArrowDownSignTo",
  };
  </script>
  
  
  <style>
  .arrow-down-sign-to {
    height: 12px;
    overflow: hidden;
    position: relative;
    width: 8px;
  }
  
  .arrow-down-sign-to .path {
    height: 12px;
    left: 2px;
    object-fit: cover;
    position: absolute;
    top: -2px;
    transform: rotate(-90deg);
    width: 8px;
  }
  </style>
  