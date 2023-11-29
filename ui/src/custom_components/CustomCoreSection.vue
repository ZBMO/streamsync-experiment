<template>
	<section 
    class="CoreSection"
	ref="rootEl" 
    :class="{ snapMode: fields.snapMode.value == 'yes' }"  
    >
		<h2 v-if="fields.title.value">{{ fields.title.value }} REAL CUSTOM</h2>
		<div data-streamsync-container v-on:click.capture="captureClick" v-on:input.capture="captureInput"><slot></slot></div>
	</section>
</template>

<script lang="ts">

import { FieldCategory, FieldType } from "../streamsyncTypes";
import {
	accentColor,
	primaryTextColor,
	secondaryTextColor,
	containerBackgroundColor,
	containerShadow,
	separatorColor,
	buttonColor,
	buttonTextColor,
	buttonShadow,
cssClasses,
} from "../renderer/sharedStyleFields";
import { assembleParameterSignals } from "vega-lite/build/src/parameter";
import { TRAIL } from "vega-lite/build/src/mark";

const description =
	"A container component that divides the layout into sections, with an optional title.";

export default {
	streamsync: {
		name: "Section",
		description,
		category: "Layout",
		allowedChildrenTypes: ["*"],
		fields: {
			title: {
				name: "Title",
				init: "Section Title",
				desc: "Leave blank to hide.",
				type: FieldType.Text,
			},
			accentColor,
			primaryTextColor,
			secondaryTextColor,
			containerBackgroundColor,
			containerShadow,
			separatorColor,
			buttonColor,
			buttonTextColor,
			buttonShadow,
			snapMode: {
				name: "Snap mode",
				type: FieldType.Text,
				options: {
					no: "No",
					yes: "Yes",
				},
				default: "no",
				init: "no",
				category: FieldCategory.Style,
				desc: "Use as much space as possible without altering the size of the container.",
			},
			cssClasses,
		},
		previewField: "title",
	},
};
</script>
<script setup lang="ts">
import { Ref, inject, ref } from "vue";
import injectionKeys from "../injectionKeys";

const ss = inject(injectionKeys.core);
const instancePath = inject(injectionKeys.instancePath);

function getComponentId(event: Event): string {
	const targetEl: HTMLElement = (event.target as HTMLElement).closest(
		"[data-streamsync-id]"
	);

	const componentId = targetEl.dataset.streamsyncId;
	return componentId
}

function isCorrectInputType(event: Event, expectedTypes): boolean {
    const type = (<HTMLInputElement>event.target).nodeName
    return expectedTypes.includes(type)
}

function captureClick(event: Event) {
    event.stopPropagation()
    if (!isCorrectInputType(event, ["BUTTON"])) { return }

	const componentId = getComponentId(event)
	const customEvent = new CustomEvent("click", {
		detail: {
			payload: {
				id: componentId,
			},
		},
	});

	ss.forwardEvent(customEvent, instancePath, true)
}

function captureInput(event: Event) {
    event.stopPropagation()
    if (!isCorrectInputType(event, ["INPUT"])) { return }

	const componentId = getComponentId(event)
	const inputValue = (<HTMLInputElement>event.target).value
	const customEvent = new CustomEvent("input", {
		detail: {
			payload: {
				id: componentId,
				value: inputValue
			},
		},
	});

	ss.forwardEvent(customEvent, instancePath, true)
}

const fields = inject(injectionKeys.evaluatedFields);
</script>

<style scoped>
@import "../renderer/sharedStyles.css";
.CoreSection {
	padding: 16px;
	border: 1px solid var(--separatorColor);
	border-radius: 8px;
	box-shadow: var(--containerShadow);
	background-color: var(--containerBackgroundColor);
}

.CoreSection.snapMode {
	flex: 1 0 auto;
	align-self: stretch;
}

h2 {
	margin-bottom: 16px;
}
</style>
