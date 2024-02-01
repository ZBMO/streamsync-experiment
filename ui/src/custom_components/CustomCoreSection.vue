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
import { METHODS } from "http";

const description =
	"A container component that divides the layout into sections, with an optional title.";

const defaultSpec = {
	$schema: "https://vega.github.io/schema/vega-lite/v5.json",
	description,
	data: {
		values: [
			{ a: "A", b: 100 },
			{ a: "B", b: 200 },
			{ a: "C", b: 150 },
			{ a: "D", b: 300 },
		],
	},
	mark: "bar",
	encoding: {
		x: { field: "a", type: "nominal" },
		y: { field: "b", type: "quantitative" },
	},
};

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
import { inject, watch, ref } from "vue";
import injectionKeys from "../injectionKeys";

const ss = inject(injectionKeys.core);
const instancePath = inject(injectionKeys.instancePath);
const fields = inject(injectionKeys.evaluatedFields);
const disablingIds = ["laser-toggle"]
const ignoreClickComponents = ["tab"]
var buttonsDisabled = false


function toggleDisableInputs(id: string, value: String) {
	if (disablingIds.includes(id)) {
		buttonsDisabled = (value == "yes") ? true : false
	}
}

function getIdentifier(event: Event): string {
	const targetEl: HTMLElement = (event.target as HTMLElement).closest(
		"[data-streamsync-id]"
	);

	var component = ss.getComponentById(targetEl.dataset.streamsyncId)
	var customId = component.content["customId"]
	var defaultId = targetEl.dataset.streamsyncId

	return (customId != "") ? customId : defaultId
}

function isCorrectInputType(event: Event, expectedTypes): boolean {
    const type = (<HTMLInputElement>event.target).nodeName	
    return expectedTypes.includes(type)
}

function ignoreClick(event) {
	const targetEl: HTMLElement = (event.target as HTMLElement).closest(
		"[data-streamsync-id]"
	);
	var component = ss.getComponentById(targetEl.dataset.streamsyncId)

	if (component["type"] in ignoreClickComponents) {
		return true
	} else {
		return false
	}
}

function captureClick(event: Event) {
	if (ignoreClick(event)) {
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
	console.log('captureChange event')
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