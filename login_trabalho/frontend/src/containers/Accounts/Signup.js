import React, { useState } from "react";
import "./index.css";
import myConfig from "../../configs/config";
import { Link, useHistory } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import { FiArrowLeft } from "react-icons/fi";
import axios from "axios";

export default function Register() {
  const [nome, setName] = useState("");
  const [senha, setsenha] = useState("");
  const [c_senha, setCsenha] = useState("");
  const [name_establishment, setEst] = useState("");

  const history = useHistory();

  function handleRegister(e) {
    e.preventDefault();

    const data = {
      nome,
      senha,
      email: nome,
    };

    let USER_URL = myConfig.API_URL + "/users/";
    axios({
      baseURL: USER_URL,
      method: "POST",
      data: data,
    })
      .then((res) => {
        if (res.status === 201) {
          toast(`Cadastro realizado com sucesso !`);
        }
        setTimeout(() => {
          history.push("/login/");
        }, 5000);
      })
      .catch((error) => {
        console.log(error);
        let error_msg = "";
        Object.keys(error.response.data).forEach(function (e) {
          error_msg += e + ": " + error.response.data[e][0] + " - ";
        });
        toast(error);
      });
  }

  return (
    <div className="signup_content">
      <div className="content">
        <section className="">
          <h1>Cadastro</h1>
        </section>
        <form onSubmit={handleRegister}>
          <input
            value={name_establishment}
            onChange={(e) => setEst(e.target.value)}
            placeholder="Nome"
          />
          <br />
          <input
            value={nome}
            onChange={(e) => setName(e.target.value)}
            placeholder="E-mail"
            type="email"
          />

          <div className="input-group">
            <input
              value={senha}
              onChange={(e) => setsenha(e.target.value)}
              placeholder="Senha"
              type="senha"
            />
          </div>

          <input
            value={c_senha}
            onChange={(e) => setCsenha(e.target.value)}
            placeholder="Confirmar senha"
            type="senha"
          />
        <br/>
          <button className="button" type="submit">
            Cadastrar
          </button>
        </form>
      </div>
      <Link to="/" className="back-link">
            <FiArrowLeft size={16} color="b366ff" />
            Já tenho cadastro
          </Link>
      <ToastContainer />
    </div>
  );
}
