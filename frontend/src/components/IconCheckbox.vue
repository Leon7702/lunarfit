<template>
    <div class="row">
      <div class="item icon-container">
        <img :src="icon" alt="Icon" class="icon">
      </div>
      <div class="item text-container">
        <span class="text">{{ text }}</span>
      </div>
      <div class="item checkbox-container">
        <input type="checkbox" class="checkbox" v-model="localChecked">
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'IconCheckbox',
    props: {
      icon: {
        type: String,
        required: true
      },
      text: {
        type: String,
        required: true
      },
      checked: {
        type: Boolean,
        default: false
      }
    },
    data() {
      return {
        localChecked: this.checked
      };
    },
    watch: {
      checked(newVal) {
        this.localChecked = newVal;
      },
      localChecked(newVal) {
        this.$emit('update:checked', newVal);
      }
    }
  };
  </script>
  
  <style scoped>
  .row {
    display: flex;
    align-items: center;
    border-bottom: 1px solid #ccc;
    padding: 10px 0;
  }
  
  .item {
    display: flex;
    align-items: center;
  }
  
  .icon-container {
    flex: 0 0 40px; /* Fixed width for the icon container */
    justify-content: center;
  }
  
  .text-container {
    flex: 1; /* Allow text to take the remaining space */
    justify-content: flex-start;
    color: #000;
    font-size: 16.32px;
    font-style: normal;
    font-weight: 400;
    line-height: 24.48px; /* 150% */
    padding-left: 15px; /* Adjust padding to ensure consistent space */
  }
  
  .checkbox-container {
    flex: 0 0 40px; /* Fixed width for the checkbox container */
    justify-content: center;
  }
  
  .icon {
    width: 30px;
    height: 30px;
  }
  
  .text {
    font-size: 16px;
  }
  
  .checkbox {
    display: block;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    appearance: none;
    background-color: #D9D9D9B8;
    position: relative;
  }
  
  .checkbox:checked {
    background-color: #50c1ba;
  }
  
  .checkbox:checked::after {
    content: '';
    display: block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #fff;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  </style>
  