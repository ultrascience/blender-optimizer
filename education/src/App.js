import React, {Suspense} from "react";
import { Canvas } from "react-three-fiber";
import Danburita from "./Danburita.js"
import Augen from "./Augen.js"
import CortezaBasalto from "./CortezaBasalto.js"
import Geoda from "./Geoda.js"
import BasaltoOxidado from "./BasaltoOxidado.js"
import Magnetita from "./Magnetita.js"
import Wulfenita from "./Wulfenita.js"
import Goethita from "./Goethita.js"
import { OrbitControls } from "@react-three/drei";
import "./index.css";

const Galeria = (props) => {
    return (
    <Canvas>
      <OrbitControls />
      <ambientLight intensity={0.6} />
      <directionalLight intensity={0.5} />
      <Suspense fallback={null}>
      {props.elemento}
      </Suspense>
  </Canvas>
);
}

export default function App() {
  return (
	  <React.Fragment>
	  <h1>Prototipo version 1.0</h1>
	  <Galeria elemento={<Danburita />} />
	  <Galeria elemento={<Augen />} />
	  <Galeria elemento={<CortezaBasalto />} />
	  <Galeria elemento={<Geoda />} />
	  <Galeria elemento={<Magnetita />} />
	  <Galeria elemento={<Wulfenita />} />
	  <Galeria elemento={<Goethita />} />

	  </React.Fragment>
  );
}

