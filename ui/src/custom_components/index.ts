
// Import the templates

import CustomSection from './CustomCoreSection.vue';
import CustomButton from './CustomCoreButton.vue';
import CustomDropDown from './inputs/CoreDropDownInput.vue';
import CustomTextInput from './inputs/CoreTextInput.vue';
import CustomVegaChart from './CustomCoreVegaLiteChart.vue';
import CustomNumberInput from './inputs/CustomNumberInput.vue';

// Export an object with the ids and the templates as default

export default {
    "customsection": CustomSection,
    "custombutton": CustomButton,
    "customdropdown": CustomDropDown,
    "customtextinput": CustomTextInput,
    "customvegachart": CustomVegaChart,
    "customnumberinput": CustomNumberInput,
}