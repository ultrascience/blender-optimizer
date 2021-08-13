/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
*/

import React, { useRef } from 'react'
import { useGLTF } from '@react-three/drei'

export default function Model(props) {
  const group = useRef()
  const { nodes, materials } = useGLTF('/Goethita.glb')
  return (
    <group ref={group} {...props} dispose={null}>
      <group position={[-0.23, 2.3, -0.1]} rotation={[-1.9, 0, 0]} scale={[8.27, 8.27, 8.27]}>
        <mesh geometry={nodes.texturedMesh_1.geometry} material={materials.TextureAtlas_0} />
        <mesh geometry={nodes.texturedMesh_2.geometry} material={materials.TextureAtlas_1} />
        <mesh geometry={nodes.texturedMesh_3.geometry} material={materials['Material.006']} />
        <mesh geometry={nodes.texturedMesh_4.geometry} material={materials['Material.004']} />
        <mesh geometry={nodes.texturedMesh_5.geometry} material={materials['Material.005']} />
      </group>
    </group>
  )
}

useGLTF.preload('/Goethita.glb')
