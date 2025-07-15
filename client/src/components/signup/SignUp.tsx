import React, {useState} from 'react';

const SignUp: React.FC = () => {

    interface SignUpGenderField {
        id: number;
        value: string;
        label: string;
    }

    const genderFields: SignUpGenderField[] = [
        {id: 1, value: 'select', label: 'Select'},
        {id: 2, value: 'male', label: 'Male'},
        {id: 3, value: 'female', label: 'Female'},
    ];


    const [formData] = useState({
        email: '',
        password: '',
        first_name: '',
        last_name: '',
        phone: '',
        address: '',
        gender: '',
        date_of_birth: '',
        tax_id: ''
    });


    return (
        <form>
            <input name="email" type="email" placeholder="Email" required value={formData.email}/>
            <input name="password" type="password" placeholder="Пароль" required value={formData.password}/>
            <input name="first_name" placeholder="Имя" value={formData.first_name}/>
            <input name="last_name" placeholder="Фамилия" value={formData.last_name}/>
            <input name="phone" placeholder="Телефон" value={formData.phone}/>
            <input name="address" placeholder="Адрес" value={formData.address}/>
            <select name="gender" value={formData.gender}>
                {genderFields.map(g => (
                    <option key={g.value} value={g.value}>
                        {g.label}
                    </option>
                ))}
            </select>
            <input name="date_of_birth" type="date" value={formData.date_of_birth}/>
            <input name="tax_id" placeholder="ИНН" value={formData.tax_id}/>

            <button type="submit">SignUp</button>
        </form>
    );
};

export default SignUp;
