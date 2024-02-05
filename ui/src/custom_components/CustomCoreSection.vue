<template>
	<section 
    class="CoreSection"
	ref="rootEl" 
    :class="{ snapMode: fields.snapMode.value == 'yes' }"
	v-on:click.capture="captureClick" 
    >
		<h2 v-if="fields.title.value">{{ fields.title.value }} CUSTOM SECTION</h2>
		<div data-streamsync-container
		v-on:input.capture="captureInput"
		v-on:change.capture="captureChange"
		><slot></slot></div>
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
import { inject } from "vue";
import injectionKeys from "../injectionKeys";

const ss = inject(injectionKeys.core);
const instancePath = inject(injectionKeys.instancePath);
const disablingIds = ["laser-toggle"]
var buttonsDisabled = false


function toggleDisableInputs(id: string, value: String) {
	if (disablingIds.includes(id)) {
		buttonsDisabled = (value == "yes") ? true : false
	}
}

function getParentTabId(target: HTMLElement): string {
	const targetEl: HTMLElement = (target as HTMLElement).closest(
		".CoreTab"
	);
	var tab = ss.getComponentById(targetEl.dataset.streamsyncId)
	var customId = tab.content["customId"]
	return customId
}

function getIdentifier(event: Event): string {
	const targetEl: HTMLElement = (event.target as HTMLElement).closest(
		"[data-streamsync-id]"
	);
	var component = ss.getComponentById(targetEl.dataset.streamsyncId)
	var targetId = component.content["customId"]
	var parentId = getParentTabId(targetEl)
	var compositeId = parentId + targetId

	var defaultId = targetEl.dataset.streamsyncId

	return (compositeId != "") ? compositeId : defaultId
}

function isCorrectInputType(event: Event, expectedTypes): boolean {
    const type = (<HTMLInputElement>event.target).nodeName	
    return expectedTypes.includes(type)
}

function ignoreTabClick(event) {
	const targetEl: HTMLElement = (event.target as HTMLElement).closest(
		"[data-streamsync-id]"
	);
	var component = ss.getComponentById(targetEl.dataset.streamsyncId)

	return component["type"].includes("tab")
}

function captureClick(event: Event) {
	console.log('captureClick: ')
	console.log(event)
	if (ignoreTabClick(event)) {
		return
	}

    event.stopPropagation()
    if (!isCorrectInputType(event, ["BUTTON"])) { return }
	if (buttonsDisabled) { return }

	const customId = getIdentifier(event)
	const customEvent = new CustomEvent("click", {
		detail: {
			payload: {
				id: customId,
			},
		},
	});
	ss.forwardEvent(customEvent, instancePath, true)
}

function captureInput(event: Event) {
	console.log('captureInput: ')
	console.log(event)
    event.stopPropagation()
    if (!isCorrectInputType(event, ["INPUT"])) { return }

	const componentId = getIdentifier(event)
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

function captureChange(event: Event) {
	console.log('captureChange: ')
	console.log(event)
	event.stopPropagation()
    if (!isCorrectInputType(event, ["SELECT", "INPUT"])) { return }

	const componentId = getIdentifier(event)
	const inputValue = (<HTMLInputElement>event.target).value
	const customEvent = new CustomEvent("change", {
		detail: {
			payload: {
				id: componentId,
				value: inputValue
			},
		},
	});


	toggleDisableInputs(componentId, inputValue)
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