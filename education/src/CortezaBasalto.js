/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
*/

import React, { useRef } from 'react'
import { useGLTF } from '@react-three/drei'

export default function Model(props) {
  const group = useRef()
  const { nodes, materials } = useGLTF('/CortezaBasalto.glb')
  return (
    <group ref={group} {...props} dispose={null}>
      <group position={[-0.03, 3.68, -0.11]} rotation={[-2.22, 0, 0]} scale={[10.64, 10.64, 10.64]}>
        <mesh geometry={nodes.texturedMesh001_1.geometry} material={materials['TextureAtlas_0.001']} />
        <mesh geometry={nodes.texturedMesh001_2.geometry} material={materials['Material.001']} />
        <mesh geometry={nodes.texturedMesh001_3.geometry} material={materials['Material.004']} />
        <mesh geometry={nodes.texturedMesh001_4.geometry} material={materials['Material.005']} />
      </group>
    </group>
  )
}

useGLTF.preload('/CortezaBasalto.glb')
