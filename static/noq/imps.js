function get(elt_id) { return document.getElementById(elt_id); }

function make_elt(type, class_name, parent, innerHTML)
{
	let elt = document.createElement(type);
	if (class_name !== undefined)
		elt.classList.add(class_name);
	if (parent !== undefined)
		parent.appendChild(elt);
	if (innerHTML !== undefined)
		elt.innerHTML = innerHTML;
	return elt;
}

class TextImp
{
	constructor(key, name, value)
	{
		this.key = key;
		this.name = name;
		this.elt = make_elt('div', 'param_div', get('params_div'), this.name);
		this.inp = make_elt('INPUT', 'param_input', this.elt);
		this.inp.setAttribute('id', `param_input_${this.key}`);
		if (key == 'r' || key == 'c' || key == 'n')
			this.inp.setAttribute('onchange', 
				`display_grid();
				this.style.width = get_text_width(this.value);`
			);

		this.set_value(value);
	}

	set_value(value)
	{
		this.value = value;
		this.inp.value = this.value;
		this.inp.style.width = get_text_width(this.value);
	}

	encode_input()
	{
		return this.inp.value;
	}
}

class CheckboxImp
{
	constructor(key, name, value=false)
	{
		this.key = key;
		this.name = name;
		this.elt = make_elt('div', 'param_div', get('params_div'), this.name);
		this.checkbox = make_elt('INPUT', 'param_input', this.elt);
		this.checkbox.setAttribute('type', 'checkbox');
		this.checkbox.setAttribute('id', `checkbox_${this.key}`);

		this.set_value(value);
	}

	set_value(value)
	{
		this.checkbox.checked = value;
	}

	encode_input()
	{
		return this.checkbox.checked;
	}
}

class DropdownImp
{
	constructor(key, name, value, options)
	{
		this.key = key;
		this.name = name;
		this.elt = make_elt('div', 'param_div', get('params_div'), this.name);
		this.dropdown = make_elt('SELECT', 'param_input', this.elt);
		this.dropdown.classList.add('imp_dropdown');
		for (const option of options) {
			const option_elt = make_elt('OPTION', 'imp_dropdown', this.dropdown);
			option_elt.value = option;
			option_elt.text = option;
		}
		this.set_value(value || options[0]);
	}

	set_value(value)
	{
		this.dropdown.value = value;
	}

	encode_input()
	{
		return this.dropdown.value;
	}
}

function builder(key, params)
{
	const name = params.name;
	const val = params.value;
	const options = params.options;
	if (params.options) {
		return new DropdownImp(key, name, val, options);
	} else if (val === true || val === false) {
		return new CheckboxImp(key, name, val); 
	} else {
		return new TextImp(key, name, val);
	}
}

let imp_types = {
	int: TextImp,
	checkbox: CheckboxImp,
	dropdown: DropdownImp,
	builder: builder
};