<template>
  <div>
    <!-- Verwendung des TextFormFields -->
    <FormFieldText label="Ihr Label hier" iconName="event" :value="initialValue" />
    
    <!-- Verwendung der StandardButton-Komponente -->
    <StandardButton label="Das ist ein Button" />
  </div>
</template>

<script>
import StandardButton from 'components/StandardButton.vue';
import FormFieldText from 'components/FormFieldText.vue';

export default {
  name: 'ExamplePage',
  components: {
    StandardButton,
    FormFieldText
  },
  data() {
    return {
      initialValue: 'Initialer Wert hier'
    };
  }
};
</script>
