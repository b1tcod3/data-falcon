package main

import (
	"reflect"
	"testing"
)

func TestNewPersonSinAmigos(t *testing.T) {
	p := NewPerson("Ana")
	if p.name != "Ana" {
		t.Errorf("name debería ser Ana, es %q", p.name)
	}
	if p.FriendsCount() != 0 {
		t.Errorf("FriendsCount() debería ser 0, es %d", p.FriendsCount())
	}
	if len(p.FriendNames()) != 0 {
		t.Errorf("FriendNames() debería estar vacío")
	}
}

func TestAddFriend(t *testing.T) {
	ana := NewPerson("Ana")
	carlos := NewPerson("Carlos")
	ana.AddFriend(carlos)

	if ana.FriendsCount() != 1 {
		t.Errorf("FriendsCount() debería ser 1, es %d", ana.FriendsCount())
	}
	if !ana.HasFriend(carlos) {
		t.Error("HasFriend(carlos) debería ser true")
	}
	got := ana.FriendNames()
	want := []string{"Carlos"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("FriendNames() = %v, esperado %v", got, want)
	}
}

func TestAddFriendSinDuplicados(t *testing.T) {
	ana := NewPerson("Ana")
	carlos := NewPerson("Carlos")
	ana.AddFriend(carlos)
	ana.AddFriend(carlos)

	if ana.FriendsCount() != 1 {
		t.Errorf("FriendsCount() debería ser 1 (sin duplicados), es %d", ana.FriendsCount())
	}
}

func TestRemoveFriend(t *testing.T) {
	ana := NewPerson("Ana")
	carlos := NewPerson("Carlos")
	beatriz := NewPerson("Beatriz")

	ana.AddFriend(carlos)
	ana.AddFriend(beatriz)
	ana.RemoveFriend(carlos)

	if ana.FriendsCount() != 1 {
		t.Errorf("FriendsCount() debería ser 1, es %d", ana.FriendsCount())
	}
	if ana.HasFriend(carlos) {
		t.Error("HasFriend(carlos) debería ser false")
	}
	if !ana.HasFriend(beatriz) {
		t.Error("HasFriend(beatriz) debería ser true")
	}
}

func TestRemoveFriendInexistente(t *testing.T) {
	ana := NewPerson("Ana")
	carlos := NewPerson("Carlos")
	ana.RemoveFriend(carlos) // no debe panic
	if ana.FriendsCount() != 0 {
		t.Errorf("FriendsCount() debería seguir 0, es %d", ana.FriendsCount())
	}
}

func TestFriendNamesOrden(t *testing.T) {
	ana := NewPerson("Ana")
	carlos := NewPerson("Carlos")
	beatriz := NewPerson("Beatriz")
	diego := NewPerson("Diego")

	ana.AddFriend(carlos)
	ana.AddFriend(beatriz)
	ana.AddFriend(diego)

	got := ana.FriendNames()
	want := []string{"Carlos", "Beatriz", "Diego"}
	if !reflect.DeepEqual(got, want) {
		t.Errorf("FriendNames() = %v, esperado %v", got, want)
	}
}

func TestAmistadBidireccional(t *testing.T) {
	ana := NewPerson("Ana")
	carlos := NewPerson("Carlos")

	ana.AddFriend(carlos)
	carlos.AddFriend(ana)

	if !ana.HasFriend(carlos) || !carlos.HasFriend(ana) {
		t.Error("la amistad debería ser bidireccional")
	}
}
