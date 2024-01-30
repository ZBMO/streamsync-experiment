<template>
	<div class="CoreNumberInput" ref="rootEl">
		<label>{{ fields.label.value }}</label>
		<input
			type="number"
			ref="inputEl"
			v-on:input="handleInputEvent"
			v-on:change="handleChangeEvent"
			:value="formValue"
			:placeholder="fields.placeholder.value"
			:min="fields.minValue.value !== null ? fields.minValue.value : undefined"
			:max="fields.maxValue.value !== null ? fields.maxValue.value : undefined"
			:step="fields.valueStep.value !== null ? fields.valueStep.value : undefined"
		/>
	</div>

	<div class="CoreVegaLiteChart" ref="rootEl">
		<div>
			
		</div>
		<div ref="chartTargetEl" class="target"></div>
	</div>
</template>

<script lang="ts">
import { FieldType } from "../streamsyncTypes";
import { cssClasses } from "../renderer/sharedStyleFields";

const description = "A component that displays Vega-Lite/Altair charts.";

const docs = `

Generate a chart using Altair and pass it via state; it'll be converted to Vega-Lite specification.

\`state["my_chart"] = chart\`

Afterwards, you can reference the chart in the specification using the syntax \`@{my_chart}\`.

Alternatively, you can work with Vega-Lite directly.
`;

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
		name: "Vega Lite Chart",
		description,
		docs,
		category: "Content",
		fields: {
			spec: {
				name: "Chart specification",
				default: JSON.stringify(defaultSpec, null, 2),
				desc: "Vega-Lite chart specification. Pass a Vega Altair chart using state or paste a JSON specification.",
				type: FieldType.Object,
			},
			customId: {
				name: "CustomId",
				init: "Input CustomId",
				type: FieldType.Text,
			},
			label: {
				name: "Label",
				init: "Input Label",
				type: FieldType.Text,
			},
			placeholder: {
				name: "Placeholder",
				type: FieldType.Text,
			},
			minValue: {
				name: "Minimum value",
				type: FieldType.Number,
				default: null
			},
			maxValue: {
				name: "Max value",
				type: FieldType.Number,
				default: null
			},
			valueStep: {
				name: "Step",
				type: FieldType.Number,
				default: "1"
			},
			cssClasses,
		},
	},
};
</script>

<script setup lang="ts">
import { inject, onMounted, Ref, ref, watch } from "vue";
import injectionKeys from "../injectionKeys";
import { useFormValueBroker } from "../renderer/useFormValueBroker";

const rootEl: Ref<HTMLElement> = ref(null);
const chartTargetEl: Ref<HTMLElement> = ref(null);
const fields = inject(injectionKeys.evaluatedFields);
const inputEl = ref(null);
const ss = inject(injectionKeys.core);
const componentId = inject(injectionKeys.componentId);

const { formValue, handleInput } = useFormValueBroker(ss, componentId, rootEl);

function enforceLimitsAndReturnValue() {
	if (inputEl.value.value == "") return null;

	let v:number = parseFloat(inputEl.value.value);
	
	if (isNaN(v)) return v;
	if (fields.minValue.value !== null && v < fields.minValue.value) {
		v = fields.minValue.value;
		inputEl.value.value = v;
	}
	if (fields.maxValue.value !== null && v > fields.maxValue.value) {
		v = fields.maxValue.value;
		inputEl.value.value = v;
	}
	return v;
}

function handleInputEvent() {
	console.log("handling handleInputEvent")
	const v = enforceLimitsAndReturnValue();
	if (isNaN(v)) return;
	handleInput(v, 'ss-number-change');
}

function handleChangeEvent() {
	console.log("handling handleChangeEvent")
	const v = enforceLimitsAndReturnValue();
	if (isNaN(v)) return;
	handleInput(v, 'ss-number-change-finish');
}

const renderChart = async () => {
	console.log("renderChart")
	if (import.meta.env.SSR) return;
	if (!fields.spec.value || !chartTargetEl.value) return;
	const { default: embed } = await import("vega-embed");
	await embed(chartTargetEl.value, fields.spec.value);
};

watch(
	() => fields.spec.value,
	(spec) => {
		if (!spec) return;
		renderChart();
	}
);

onMounted(() => {
	renderChart();
	new ResizeObserver(renderChart).observe(rootEl.value, {
		box: "border-box",
	});
});
</script>

<style scoped>
@import "../renderer/sharedStyles.css";

.CoreVegaLiteChart {
	min-height: 1px;
}

.target {
	overflow: hidden;
}

</style>
