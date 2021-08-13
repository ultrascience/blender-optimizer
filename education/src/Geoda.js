/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
*/

import React, { useRef } from 'react'
import { useGLTF } from '@react-three/drei'

export default function Model(props) {
  const group = useRef()
  const { nodes, materials } = useGLTF('/Geoda.glb')
  return (
    <group ref={group} {...props} dispose={null}>
      <group position={[-0.04, 4.87, 0.21]} rotation={[-1.56, 0, 0.47]} scale={6.91}>
        <mesh geometry={nodes.texturedMesh_1.geometry} material={materials.TextureAtlas_0} />
        <mesh geometry={nodes.texturedMesh_2.geometry} material={materials.TextureAtlas_1} />
        <mesh geometry={nodes.texturedMesh_3.geometry} material={materials.TextureAtlas_2} />
        <mesh geometry={nodes.texturedMesh_4.geometry} material={materials.TextureAtlas_3} />
        <mesh geometry={nodes.texturedMesh_5.geometry} material={materials.TextureAtlas_4} />
        <mesh geometry={nodes.texturedMesh_6.geometry} material={materials['Material.002']} />
        <mesh geometry={nodes.texturedMesh_7.geometry} material={materials['Material.004']} />
        <mesh geometry={nodes.texturedMesh_8.geometry} material={materials['Material.005']} />
      </group>
    </group>
  )
}

useGLTF.preload('/Geoda.glb')
